import commands
import DD
import js
import os
import random
import re
import time
import tempfile
import argparse
import subprocess
from coverage import Coverage
from myutil import *
import jsconstant
import glob




class TimeoutError(Exception):
    pass


class XX:
    file_line = {}


class NonAdq(DD.DD):
    YAFFS = 0
    JS = 1
    GZIP = 2
    GREP = 3
    GCC  = 4
    
    NMUT = 0
    CCOV = 1

    def __init__(self, path, sut, deltas, mutants, gcov_dir, gcov_exe, oracle, gcov_files):
        DD.DD.__init__(self)
        self.path = path
        self.sut = sut
        self.deltas = deltas[:]
        self.gcov_dir = gcov_dir
        self.gcov_exe = gcov_exe
        self.oracle = oracle
        self.mutants = mutants
        self.gcov_files = sorted(gcov_files)
        self.lineCov = self.getCoverage(deltas)
        self.detectedMutants = self.getMutants(deltas)
        print 'detected:', len(self.detectedMutants)
        print 'all:', len(mutants)


    def runWith(self, executable, deltas):
        out = ''

        
        if self.sut == NonAdq.GREP:
            # print deltas
            d = ''.join(map(lambda s:s[1], deltas))
            cmd = 'timeout 1 {0} {1} {2}'.format(executable, d, "grepsrc/grep1.dat")
            out = ex(cmd)    
            print cmd

        if self.sut == NonAdq.YAFFS:
            s = '\n'.join(map(lambda s: s[1],deltas))
            f = tempfile.NamedTemporaryFile(mode='w+t')
            testpath = f.name
            f.write(s)
            f.flush()
            cmd = "timeout 1 {0} {1}".format(executable, testpath)
            out = ex(cmd)

        if self.sut == NonAdq.JS:

            s = jsconstant.prefix + '\n'
            s += '\n'.join(map(lambda s: s[1],deltas))
            f = tempfile.NamedTemporaryFile(mode='w+t',suffix='.js')
            testpath = f.name
            f.write(s)
            f.flush()
            print s
            cmd = "timeout 3 {0} -f {1}".format(executable, testpath)
            out  = ex(cmd)
            print cmd, out
            #pattern = re.compile("before [0-9]+, after [0-9]+, break [0-9a-f]+")
            #return pattern.sub('', out)

        if self.sut == NonAdq.GZIP:
            s = ''.join(deltas)
            f.write(s)
            f.flush()
            cmd1 = "rm -f {0}.gz".format(testpath)
            cmd2 = "timeout 1 {0} {1}".format(executable, testpath)
            cmd3 = "rm -f {0}".format(testpath)
            cmd4 = "timeout 3 {0} -d {1}.gz".format(executable, testpath)
            for c in [cmd1, cmd2, cmd3, cmd4]:
                out += ex(c)
            if os.path.exists(testpath):
                f  = open(testpath)
                dd = f.read()
                if dd == s:
                    out += 'OK!'
                else:
                    out += 'NO!'

        if self.sut == NonAdq.GCC:
            f = tempfile.NamedTemporaryFile(mode='w+t', suffix='.c')
            testpath = f.name
            s = '\n'.join(deltas)
            f.write(s)
            f.flush()
            cmd = "{0} -I /home/maalipou/tools/csmith/include/csmith-2.3.0 -O3 {1}".format(executable, testpath)
            out = ex(cmd)
        return out

    cache = {}
    def getOracleOut(self, deltas):
        s = '\n'.join(deltas)
        if s in NonAdq.cache:
            return NonAdq.cache[s]
        e = self.runWith(self.oracle, deltas)
        NonAdq.cache[s] = e
        return e

    def getCoverage(self, deltas):
        cmd = "rm -f {0}/*.gcov {0}/*.gcda".format(self.gcov_dir)
        ex(cmd)
        for f in self.gcov_files:
            cmd = "rm -f {0}/{1}.gcov {0}/{1}.gcda".format(self.gcov_dir, f)
            ex(cmd)
            
        rets = []
        self.runWith(self.gcov_dir + "/" + self.gcov_exe, deltas)
        gcnos = glob.glob(self.gcov_dir + "/*gcno")
       
        for f in gcnos:
            f = f.split(os.sep)[-1]
            ret = subprocess.call (['gcov', f], cwd=self.gcov_dir, stdout=FNULL,  stderr=FNULL)
            rets.append(ret)
            # print f, ret
        
        cov = []
        for gf in sorted(self.gcov_files):
            f = os.path.join(self.gcov_dir, gf)
            temp = []
            try:
                with open(f) as gcovfile:
                    for l in gcovfile.readlines():
                        l = l.strip()
                        if l.startswith('####'): # or l.startswith('-'):
                            temp.append(0)
                        elif l[0].isdigit():
                            temp.append(1)
            except IOError:
                print 'FIle {0} was not found.'.format(f)
                pass
        
            if gf in XX.file_line and len(temp) == 0:
                temp = [0 for i in range(XX.file_line[gf])]
            if gf not in XX.file_line:
                XX.file_line[gf] = len(temp)
 
        
            cov = cov + temp       
        #print sum(cov)
        #print file_line
        
        return Coverage(cov)

    def detects(self, deltas, m):
        oracleout = self.getOracleOut(deltas)
        mout = self.runWith(m, deltas)
        if oracleout != mout:
            return True
        else:
            return False

    def getMutants(self, deltas):
        detectedMutants = []
        for m in self.mutants:
             if self.detects(deltas, m):
                detectedMutants.append(m)
        return detectedMutants

   
    def checkCov(self, deltas, c):
        newcov = self.getCoverage(deltas)
        if newcov.isSimilar(self.lineCov, c):
            return self.FAIL
        else:
            return self.PASS


    def init(self):

        self.__resolving = 0
        self.__last_reported_length = 0
        self.monotony = 0
        self.outcome_cache  = DD.OutcomeCache()
        self.cache_outcomes = 1
        self.minimize = 1
        self.maximize = 1
        self.assume_axioms_hold = 1
        self.starttime = time.time()

    def coerce(self, deltas):
        if self.sut == NonAdq.YAFFS or self.sut == NonAdq.JS:
            return '\n'.join(map(lambda p:p[1],deltas))
        if self.sut == NonAdq.GREP or self.sut == NonAdq.GZIP:
            return ''.join(map(lambda p:p[1],deltas))
        raise NotImplementedError


    checkfunc = None
    checkfunc_arg = None


    def nmutcheck(self, deltas, mutants):
        for m in mutants:
            if not self.detects(deltas, m):
                return self.PASS
        return self.FAIL


    def ccoverage(self,  c):
        self.init()
        self.checkfunc = self.checkCov
        self.checkfunc_arg = c
        return self.ddmin(self.deltas)


    def nmutant(self,  n):
        self.init()
        self.checkfunc = self.nmutcheck
        self.METHOD = NonAdq.NMUT
        random.shuffle(self.detectedMutants)
        self.targetMutants  = self.detectedMutants[:n]
        self.checkfunc_arg = self.targetMutants
        return self.ddmin(self.deltas)


    def checkListCoverage(self, deltas, l):
        newCov  = self.getCoverage(deltas)
        if newCov.contains(l):
            return self.FAIL
        else:
            return self.PASS

    def ccoverageList(self, cList):
        self.init()
        self.checkfunc = self.checkListCoverage
        self.checkfunc_arg = cList
        return self.ddmin(self.deltas)


    def _test(self, deltas):
        # returns either self.PASS, self.FAIL, or self.UNRESOLVED.
        #if time.time() - self.starttime > 1800: # 30 minute timout
        #    raise TimeoutError('Timeout!')
        if deltas == []:
            return self.PASS
        return self.checkfunc(deltas, self.checkfunc_arg)






def prepare(tc, sutStr):

    tcfile = open(tc)
    import subprocess
    
    if sutStr == 'grep':
        sut = NonAdq.GREP
        gcov_dir = "grepsrc"
        gcov_exe = "grep.exe"
        oracle = gcov_dir + "/" + gcov_exe
        cmdline = []
        gcov_files = ['grep.c.gcov']
        for c in tcfile.read().strip():
            cmdline.append(c)
        deltas = zip(range(len(cmdline)),cmdline)
        ex('git clone --depth 1 https://github.com/osustarg/grepsrc.git')
        p = subprocess.Popen(['make', 'build'], cwd='grepsrc')
        p.wait()

    elif sutStr == 'gzip':
        sut = NonAdq.GZIP
        gcov_dir = "gzipsrc"
        gcov_exe = "gzip"
        oracle = gcov_dir + "/" + gcov_exe
        deltas = []
        gcov_files = []
        for c in tcfile.read().strip():
            deltas.append(c)
        ex('git clone --depth 1 https://github.com/osustarg/gzipsrc.git')
        p = subprocess.Popen(['./configure'], cwd='gzipsrc')
        p.wait()
        p = subprocess.Popen(['make'], cwd='gzipsrc')
        p.wait()


    elif sutStr == 'yaffs':
        sut = NonAdq.YAFFS
        gcov_dir = "yaffstest/yaffs2tester"
        gcov_exe = "yaffs2_gcov"
        gcov_files = ['yaffs2.c.gcov']
        oracle = gcov_dir + "/" + gcov_exe
        lines = map(lambda s: s.strip(), tcfile.readlines())
        deltas= zip(range(len(lines)), lines) 
        if not os.path.exists('yaffstest'):
            ex('git clone --depth 1 https://github.com/alipourm/yaffstest.git')
        p = subprocess.Popen(['make', '-f',  'TestMakefile'], cwd='yaffstest/yaffs2tester')
        p.wait()


    elif sutStr == 'js':
        sut = NonAdq.JS
        gcov_dir = "spidermonkey/js1.6/src/Linux_All_DBG.OBJ"
        gcov_exe = "js"
        gcov_files = [
            'jsapi.c.gcov',
            'jsarena.c.gcov',
            'jsarray.c.gcov',
#            'Jsatom.c.gcov',
            'jsbool.c.gcov',
            'js.c.gcov',
            'jscntxt.c.gcov',
 #           'jscpucfg.c.gcov',
            'jsdate.c.gcov',
            'jsdbgapi.c.gcov',
            'jsdhash.c.gcov',
            'jsdtoa.c.gcov',
            'jsemit.c.gcov',
            'jsexn.c.gcov',
            'jsfun.c.gcov',
            'jsgc.c.gcov',
            'jshash.c.gcov',
            'jsinterp.c.gcov',
            'jslog2.c.gcov',
            'jsmath.c.gcov',
            'js.msg.gcov',
            'jsnum.c.gcov',
            'jsobj.c.gcov',
            'jsopcode.c.gcov',
            'jsparse.c.gcov',
            'jsprf.c.gcov',
            'jsregexp.c.gcov',
            'jsscan.c.gcov',
            'jsscope.c.gcov',
            'jsscript.c.gcov',
            'jsstr.c.gcov',
            'jsutil.c.gcov',
            'jsxdrapi.c.gcov',
            'jsxml.c.gcov',
            'prmjtime.c.gcov'
        ]
        oracle = gcov_dir + "/" + gcov_exe
        lines = map(lambda s: s.strip(), tcfile.readlines()) 
        deltas = zip(range(len(lines)), lines)
        ex('git clone --depth 1 https://github.com/osustarg/spidermonkey.git')
        p = subprocess.Popen(['make', '-f', 'Makefile.ref'], cwd='spidermonkey/js1.6/src/')
        p.wait()


    elif sutStr == 'gcc':
        GCCTARFILEPATH = 'gcc.sh'
        sut = NonAdq.GCC
        gcov_dir = ""
        gcov_exe = "gcc"
        gcov_files = []
        oracle = "gcc"
        deltas = map(lambda s: s.strip(), tcfile.readlines())
        ex('bash {0}'.format(GCCTARFILEPATH))






        
    tcfile.close()
    return  sut, deltas, gcov_dir,gcov_exe,oracle, gcov_files




def m():
    parser = argparse.ArgumentParser()
    parser.add_argument('-sut', required=True)
    parser.add_argument('-tc', required=True)
    parser.add_argument('-mutfile', required=True)
    args = parser.parse_args()
    tc = args.tc
    sutStr = args.sut
    mutantFile = args.mutfile
    sut, delta, gcov_dir,gcov_exe,oracle,gcov_files = prepare(tc, sutStr)


    mutants = map(lambda s:s.strip(), open(mutantFile).readlines())
    myDD = NonAdq(tc, sut, delta, mutants, gcov_dir, gcov_exe, oracle, gcov_files)
    
    myDD.experiment()
