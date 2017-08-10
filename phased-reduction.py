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
    print gcov_files
    myDD = NonAdq(tc, sut, deltas, mutants, gcov_dir, gcov_exe, oracle, gcov_files)
    originalCoverage      = myDD.getCoverage(deltas)
    d1 = deltas[:]
    print sum(originalCoverage.coverage)

    print  ex('cp {0}/{1} t1.gcov'.format(gcov_dir, gcov_files[0]))






    # phase 1
    start = time.time()
    firstPhaseTC     = myDD.ccoverage(C)
    phaseOneCoverage   = myDD.getCoverage(firstPhaseTC)


    # calculate requirement for phase 2
    d2 = deltas[:]
    originalCoverage2      = myDD.getCoverage(deltas)

    print  ex('cp {0}/{1} t2.gcov'.format(gcov_dir, gcov_files[0]))

    secondPhaseReq   = originalCoverage - phaseOneCoverage

    
    # phase 2
    myDD = NonAdq(tc, sut, d1, mutants, gcov_dir, gcov_exe, oracle, gcov_files)
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



    print 'elapsed phased:', elapsedPhased
    print 'phased diff percent:', phasedTotalCoverage.diff_percent(originalCoverage)
    print 'phased diff val:', phasedTotalCoverage.diff_val(originalCoverage)
    print 'phased TCLen Total', phasedTotalLen
    print 'phase 1 TCLen Total', len(firstPhaseTC)
    print 'phase 2 TCLen Total', len(phaseTwoTC )


    open(out1, 'w').write(myDD.coerce(firstPhaseTC))
    open(out2, 'w').write(myDD.coerce( phaseTwoTC))



if  __name__ == '__main__':
    main()
