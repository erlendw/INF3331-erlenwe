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

new = highlight

for key in syntax:

    if(isinstance(syntax[key], list)):

        for item in syntax[key]:
            pattern = "\\b" + item + "\\b"

            toignore = (re.finditer("['\"].*(\\b" + item + "\\b).*['\"]",highlight))

            occurences = (re.finditer(pattern,highlight))

            for occurence in occurences:

                print(occurence)

                '''

                for ignore in toignore:

                    if not(occurence.span()[0] > ignore.span()[0] and occurence.span()[1] < ignore.span()[1] ):

                        replaced = re.sub('\\b'+ pattern +'\\b',  color(pattern, theme[key]), new)
                        new = replaced
                '''




print(new)