import commands
import DD
import js
import os
import random
import time


class TimeoutError(Exception):
    pass


FNULL = open(os.devnull, 'w')
def ex(cmd):
    # print(cmd)
    status, output = commands.getstatusoutput(cmd)
    # print output
    return str(status) + '--' + output



import tempfile

def log(s):
    print s
    pass

class NonAdq(DD.DD):
    YAFFS = 0
    JS = 1
    GZIP = 2
    GREP = 3

    def runWith(self, executable, deltas):
        out = ''
        f = tempfile.NamedTemporaryFile(mode='w+t')
        testpath = f.name
        # log('executable: ' + executable)
        if self.sut == NonAdq.GREP:
            cmd = 'timeout 1 {0} {1} {2}'.format(executable, ''.join(deltas), "grepsrc/grep1.dat")
            out = ex(cmd)

        if self.sut == NonAdq.YAFFS:
            s = '\n'.join(deltas)
            f.write(s)
            f.flush()
            cmd = "timeout 1 {0} {1}".format(executable, testpath)
            out = ex(cmd)

        if self.sut == NonAdq.JS:
            s = js.prefix + '\n' + '\n'.join(deltas)
            f.write(s)
            f.flush()
            cmd = "timeout 1 {0} -f {1}".format(executable, testpath)

            out = ex(cmd)

        if self.sut == NonAdq.GZIP:
            s = ''.join(deltas)
            f.write(s)
            f.flush()
            cmd1 = "rm -f {0}.gz".format(testpath)
            cmd2 = "timeout 1 {0} {1}".format(executable, testpath)
            cmd3 = "rm -f {0}".format(testpath)
            cmd4 = "timeout 1 {0} -d {1}.gz".format(executable, testpath)



            for c in [cmd1, cmd2, cmd3, cmd4]:
                out += ex(c)

            if os.path.exists(testpath):
                f  = open(testpath)
                dd = f.read()
                if dd == s:
                    out += 'OK!'
                else:
                    out += 'NO!'
                f.close()

        # f.close()
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
        import glob

        cmd = "rm -f {0}/*.gcov {0}/*.gcda".format(self.gcov_dir)
        ex(cmd)
        self.runWith(self.gcov_dir + "/" + self.gcov_exe, deltas)
        gcnos = glob.glob(self.gcov_dir + "/*gcno")
        log('calcov')

        for f in gcnos:
            f = f.split(os.sep)[-1]
            ret = subprocess.call(['gcov', f], cwd=self.gcov_dir, stdout=FNULL)


        gcovs = sorted(glob.glob(self.gcov_dir + "/*.gcov"))
        # if self.sut == NonAdq.YAFFS:
        #     gcovs = ['yaffstest/yaffs2tester/yaffs2.c.gcov']
        # if self.sut == NonAdq.GREP:
        #     gcovs = ['grepsrc/grep.c.gcov']
        cov = []
        for f in gcovs:
            # print 'GCOV', f
            with open(f) as gcovfile:
                for l in gcovfile.readlines():
                    l = l.strip()
                    if l.startswith('####'):# or l.startswith('-'):
                        cov.append(0)
                    elif l[0].isdigit():
                        cov.append(1)
                gcovfile.close()
        cmd = "rm -f {0}/*.gcov {0}/*.gcda".format(self.gcov_dir)
        ex(cmd)
        print 'LEN', len(cov), sum(cov)
        return cov


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




    def __init__(self, path, sut, deltas, mutants, gcov_dir, gcov_exe, oracle):
        DD.DD.__init__(self)
        self.path = path
        self.sut = sut
        self.deltas = deltas
        self.gcov_dir = gcov_dir
        self.gcov_exe = gcov_exe
        self.oracle = oracle
        self.mutants = mutants
        self.lineCov = self.getCoverage(deltas)
        self.detectedMutants = self.getMutants(deltas)
        print 'detected:', len(self.detectedMutants)
        print 'all:', len(mutants)







    def checkCov(self, deltas, C):

        newcov = self.getCoverage(deltas)
        if len(newcov) != len(self.lineCov):
            return False
        matches = 0

        total = len(newcov)
        for i in range(total):
            if newcov[i] == self.lineCov[i]:
                matches += 1
        if float(matches)*100./total >= C:
            return True
        else:
            return False

    NMUT = 0
    CCOV = 1

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
            return '\n'.join(deltas)
        if self.sut == NonAdq.GREP or self.sut == NonAdq.GZIP:
            return ''.join(deltas)  
        raise NotImplementedError

    def experiment(self):
        for c in [60,70,80,90,95,100]:
            self.init()
            self.METHOD = NonAdq.CCOV
            self.C = c
            try:
                result = self.ddmin(self.deltas)
                s = self.coerce(result)
                open(self.path + '.{0}.C'.format(c), 'w').write(s)
                coverage = self.getCoverage(result)
                detectedMut = self.getMutants(result)
                open(self.path + '.{0}.C.cov'.format(c), 'w').write(map(lambda n: str(n), coverage))
                open(self.path + '.{0}.C.mut'.format(c), 'w').write('\n'.join(sorted(detectedMut)))

                print 'RES:', c, len(result)

            except TimeoutError:
                pass
        for m in [1, 2, 4, 8, 16, 32]:
            self.init()
            self.METHOD = NonAdq.NMUT
            random.shuffle(self.detectedMutants)
            self.targetMutants  = self.detectedMutants[:m]
            try:
                result = self.ddmin(self.deltas)
                s = self.coerce(result)
                open(self.path + '.{0}.M'.format(c), 'w').write(s)
                coverage = self.getCoverage(result)
                detectedMut = self.getMutants(result)
                open(self.path + '.{0}.M.cov'.format(m), 'w').write(''.join(map(lambda n: str(n), coverage)))
                open(self.path + '.{0}.M.mut'.format(m), 'w').write('\n'.join(sorted(detectedMut)))

                print 'RES:', m, len(result)
            except TimeoutError:
                pass

    def _test(self, deltas):
        # returns either self.PASS, self.FAIL, or self.UNRESOLVED.
        if time.time() - self.starttime > 1800: # 30 minute timout
            raise TimeoutError('Timeout!')
        if deltas == []:
            return self.PASS

        if self.METHOD == NonAdq.NMUT:
            for m in self.targetMutants:
                if not self.detects(deltas, m):
                    return self.PASS
            return self.FAIL

        if self.METHOD == NonAdq.CCOV:
            if self.checkCov(deltas, self.C):
                # print '##', deltas, self.C
                return self.FAIL
            else:
                # print '##', deltas, self.C
                return self.PASS

        return self.UNRESOLVED




import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-sut', required=True)
    parser.add_argument('-tc', required=True)
    parser.add_argument('-mutfile', required=True)
    args = parser.parse_args()
    tc = args.tc
    sutStr = args.sut
    mutantFile = args.mutfile

    tcfile = open(tc)
    import subprocess
    if sutStr == 'grep':
        sut = NonAdq.GREP
        gcov_dir = "grepsrc"
        gcov_exe = "grep.exe"
        oracle = gcov_dir + "/" + gcov_exe
        deltas = []
        for c in tcfile.read().strip():
            deltas.append(c)
        ex('git clone --depth 1 https://github.com/osustarg/grepsrc.git')
        p = subprocess.Popen(['make', 'build'], cwd='grepsrc', shell=True)
        p.wait()

    if sutStr == 'gzip':
        sut = NonAdq.GZIP
        gcov_dir = "gzipsrc"
        gcov_exe = "gzip"
        oracle = gcov_dir + "/" + gcov_exe
        deltas = []
        for c in tcfile.read().strip():
            deltas.append(c)
        ex('git clone --depth 1 https://github.com/osustarg/gzipsrc.git')
        p = subprocess.Popen(['./configure'], cwd='gzipsrc')
        p.wait()
        p = subprocess.Popen(['make'], cwd='gzipsrc')
        p.wait()


    if sutStr == 'yaffs':
        sut = NonAdq.YAFFS
        gcov_dir = "yaffstest/yaffs2tester"
        gcov_exe = "yaffs2_gcov"
        oracle = gcov_dir + "/" + gcov_exe
        deltas = map(lambda s: s.strip(), tcfile.readlines())
        ex('git clone --depth 1 https://github.com/alipourm/yaffstest.git')
        p = subprocess.Popen(['make', '-f',  'TestMakefile'], cwd='yaffstest/yaffs2tester')
        p.wait()


    if sutStr == 'js':
        sut = NonAdq.JS
        gcov_dir = "spidermonkey/js1.6/src/Linux_All_DBG.OBJ"
        gcov_exe = "js"
        oracle = gcov_dir + "/" + gcov_exe
        deltas = map(lambda s: s.strip(), tcfile.readlines())
        ex('git clone --depth 1 https://github.com/osustarg/spidermonkey.git')
        p = subprocess.Popen(['make', '-f', 'Makefile.ref'], cwd='spidermonkey/js1.6/src/')
        p.wait()

    tcfile.close()

    mutants = map(lambda s:s.strip(), open(mutantFile).readlines())
    myDD = NonAdq(tc, sut, deltas, mutants, gcov_dir, gcov_exe, oracle)

    print myDD.detects(deltas, gcov_dir + '/' + gcov_exe)

    print myDD.checkCov(['0', '1,/yaffs2'], 100)

    myDD.experiment()



    # (c, c1, c2) = dd.ddmin(deltas)	# Invoke DD
    #print c1, "passes,", c2, "fails"
