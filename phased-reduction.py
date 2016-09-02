from nonadequate import *
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-sut', required=True)
    parser.add_argument('-tc', required=True)
    parser.add_argument('-mutfile', required=True)
    args = parser.parse_args()
    tc = args.tc
    sutStr = args.sut
    mutantFile = args.mutfile
    sut, deltas, gcov_dir,gcov_exe,oracle, gcov_files = prepare(tc, sutStr)
    mutants = [] # map(lambda s:s.strip(), open(mutantFile).readlines())
    print gcov_files
    myDD = NonAdq(tc, sut, deltas, mutants, gcov_dir, gcov_exe, oracle, gcov_files)


    originalCoverage      = myDD.getCoverage(deltas)
    print  ex('cp {0}/{1} t1.gcov'.format(gcov_dir, gcov_files[0]))




    start = time.time()
    # phase 1
    firstPhaseTC     = myDD.ccoverage(70)
    phaseOneCoverage   = myDD.getCoverage(firstPhaseTC)


    # calculate requirement for phase 2

    originalCoverage2      = myDD.getCoverage(deltas)
    print ex('cp {0}/{1} t2.gcov').format(gcov_dir, gcov_files[0])
    print sum(originalCoverage.coverage), sum(originalCoverage2.coverage)
    assert originalCoverage.contains(originalCoverage2)


    secondPhaseReq   = originalCoverage - phaseOneCoverage

    # phase 2
    phaseTwoTC = myDD.ccoverageList(secondPhaseReq)
    elapsedPhased = time.time() - start

    phaseTwoCoverage = myDD.getCoverage(phaseTwoTC)
    phasedTotalCoverage = phaseOneCoverage + phaseTwoCoverage
    phasedTotalLen =  len(firstPhaseTC) + len(phaseTwoTC)




    # adequate reduction
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

    # print firstPhaseTC
    # print '---'
    # print phaseTwoTC

    print 'elapsed adeq:', elapsedAdeq
    print 'adeq diff percent:', adeqCoverage.diff_percent(originalCoverage)
    print 'adeq diff val:', adeqCoverage.diff_val(originalCoverage)
    print 'adeq TCLen Total', adeqTCLen
    # print adeqTC




if  __name__ == '__main__':
    main()






