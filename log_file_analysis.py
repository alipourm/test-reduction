#!/usr/bin/python
import sys
logfile = open(sys.argv[1])


def extractCov(line):
    line = line.strip()
    covVec = line.split()[1]
    cov = []
    for c in covVec:
        if c == '1':
            cov.append(1)
        elif c == '0':
            cov.append(0)
    return cov



keywords = [
    'C',
    'elapsedTime',
    'phaseOneLen',
    'phaseTwoLen',
    'out1Cov',
    'tcCov',
    'out1Cov',
    'out2Cov'
    ]


def sub(arr1, arr2):
    return [arr1[i] - arr2[i] for i in range(len(arr2))]

def add(arr1, arr2):
    return [max(arr1[i], arr2[i]) for i in range(len(arr2))]

import math
def xor(arr1, arr2):
    return [arr1[i]^ arr2[i] for i in range(len(arr2))]


lines = logfile.readlines()
covTotal = extractCov(lines[7])
cov1 = extractCov(lines[8])
cov2 = extractCov(lines[9])


covPhased = add(cov1, cov2)
print 'sum(xor)', sum(xor(cov2, covPhased))
# print xor(cov2, cov1)
print 'sum(cov1) = ', sum(cov1)
print 'sum(cov2) = ', sum(cov2)
print 'sum(covTotal) = ', sum(covTotal)

