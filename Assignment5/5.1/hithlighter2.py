import sys
import json
import re
from colors import color

syspath = sys.path[0] + "/"

args = sys.argv

args.pop(0)

syntaxfile_in = syspath + args[0] + ".json"
themefile_in = syspath + args[1] + ".json"
highlightfile_in = syspath + args[2]


with open(syntaxfile_in) as data:
    syntax = json.load(data)

with open(themefile_in) as data:
    theme = json.load(data)

with open(highlightfile_in, 'r') as data:
    highlight = data.read()






