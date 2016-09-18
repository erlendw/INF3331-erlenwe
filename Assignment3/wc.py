import sys
import os.path as path
import glob
import re

args = sys.argv
args.pop(0) ##fjerner scriptet selv
syspath = sys.path[0] + "/"

if args[0]=='*':
    args=(glob.glob(syspath + '*'))
    syspath = ''


def lineNum(path):
    with open(filepath,'r') as f:
            lines = f.readlines()
            f.close()

    return len(lines)

def wordNum(path):

    with open(filepath,'r') as f:
            filestring = f.read()
            f.close()

    filestring=re.sub('[^A-Za-z0-9]+', ' ', filestring)
    filestring=re.sub('\S*\d\S*', '', filestring)

    filestring=filestring.split()
    wordcount=len(filestring)
    return wordcount


for i in range(len(args)):
    filepath = syspath + args[i]

    if path.isfile(filepath):
        print("Number of lines " + str(lineNum(filepath)) + "  Number of words " + str(wordNum(filepath))
              + " filename " + args[i])