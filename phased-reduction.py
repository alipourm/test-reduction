from nonadequate import NonAdq, prepare, ex
import time
import argparse





def log(s):
    logfile.write(s + '\n')




def main():
    global logfile
    parser = argparse.ArgumentParser()
    parser.add_argument('-sut', required=True)
    parser.add_argument('-tc', required=True)
    parser.add_argument('-c', required = True)
    parser.add_argument('-out1', required = True)
    parser.add_argument('-out2', required = True)
    parser.add_argument('-log', required = True)
    
    # parser.add_argument('-mutfile', required=True)
    args = parser.parse_args()
    sutStr = args.sut
    tc = args.tc
    C = int(args.c)
    out1 = args.out1
    out2 = args.out2
    logfilename = args.log
    logfile = open(logfilename, 'w')

    log(tc)
    # mutantFile = args.mutfile
    mutants = [] 
    sut, deltas, gcov_dir,gcov_exe,oracle, gcov_files = prepare(tc, sutStr)     
    
    myDD = NonAdq(tc, sut, deltas, mutants, gcov_dir, gcov_exe, oracle, gcov_files)
    originalCoverage      = myDD.getCoverage(deltas)
    d1 = deltas[:]
    
    # phase 1
    start = time.time()
    firstPhaseTC     = myDD.ccoverage(C)
    phaseOneCoverage   = myDD.getCoverage(firstPhaseTC)

    # calculate requirement for phase 2
    d2 = deltas[:]
    secondPhaseReq   = originalCoverage - phaseOneCoverage
    #print 'second-original:',secondPhaseReq.diff_val(originalCoverage)
    #print originalCoverage.contains(secondPhaseReq)
    #print 'starting phase 2'
    # phase 2
    myDD = NonAdq(tc, sut, d2, mutants, gcov_dir, gcov_exe, oracle, gcov_files)
    
    phaseTwoTC = myDD.ccoverageList(secondPhaseReq)
    elapsedPhased = time.time() - start

    phaseTwoCoverage = myDD.getCoverage(phaseTwoTC)
    phasedTotalCoverage = phaseOneCoverage + phaseTwoCoverage
    phasedTotalLen =  len(firstPhaseTC) + len(phaseTwoTC)
  
    # start = time.time()
    # adeqTC     = myDD.ccoverageList(originalCoverage)
    # adeqCoverage   = myDD.getCoverage(adeqTC)
    # elapsedAdeq = time.time() - start
    # adeqTCLen = len(adeqTC)


    log('C: {0}'.format(C))
    log('elapsedTime: {0}'.format(elapsedPhased))
    log('phaseOneLen: {0}'.format(len(firstPhaseTC)))
    log('phaseTwoLen: {0}'.format(len(phaseTwoTC)))
    log('out1: {0}'.format(out1))
    log('out2: {0}'.format(out2))
    log('tcCov: {}'.format(originalCoverage))
    log('out1Cov: {}'.format(phaseOneCoverage))
    log('out2Cov: {}'.format(phaseTwoCoverage))
    
    
    

    open(out1, 'w').write(myDD.coerce(firstPhaseTC))
    open(out2, 'w').write(myDD.coerce( phaseTwoTC))



if  __name__ == '__main__':
    main()
