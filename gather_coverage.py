from BitVector import BitVector
import glob
import os
import re
import sys


directory = sys.argv[1]

size = 0

def toBV(s):
    arr = []
    for c in s:
        if c == '1':
            arr.append(1)
        if c == '0':
            arr.append(0)
    return arr
p = 0


import os
mut = {}
coverage = {}
for f in os.listdir(directory):
    if f.endswith('mut'):

        pattern = re.compile(r'TC[0-9]*\.([0-9]*)')
        g = pattern.search(f)
        c = g.group(1)
        if f.endswith('cov'):

            print f, c

        if f.endswith('mut'):
            mut.setdefault(c, set())
            mut[c] = mut[c] | set(open(os.path.join(directory,f)).read().split('\n'))
for c in mut:
    print c, len(mut[c])



exit()

for i in glob.glob(pattern):
#    print i
    f = open(i)
    content = f.read().strip()
    f.close()
    ct = toBV(content)

    if size == 0:
        size = len(ct)
        bv = BitVector(bitlist=ct)
    elif size!= len(ct):
        continue
    p += 1
    bv = bv | BitVector(bitlist=ct)



cov = 0
if p > 0:
    stp = str(bv)
    for c in stp:
        if c == '1':
            cov += 1.0

    print  cov/len(stp), p
else:
 print '-',  p
