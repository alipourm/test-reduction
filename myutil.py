import commands
import os

FNULL = open(os.devnull, 'w')
def ex(cmd):
    status, output = commands.getstatusoutput(cmd)
    return str(status) + '--' + output

def log(s):
    print s
