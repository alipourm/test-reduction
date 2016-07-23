#!/usr/bin/python
import argparse
import commands
parser = argparse.ArgumentParser()

parser.add_argument("--sut")
# parser.add_argument("--name")
args = parser.parse_args()
sut = args.sut
#jobname = args.name
cmd = 'qsub -v "SUT={0}" -N "{1}" commonpy.sh'.format(sut, sut)
print commands.getstatusoutput(cmd)
