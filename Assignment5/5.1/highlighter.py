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
ignorecase = syntax['ignorecase']
print(ignorecase)
for key in syntax:

    if(isinstance(syntax[key], list)):

        for i in range(len(syntax[key])):
            pattern = (syntax[key][i])
            color_ = int(theme[key])
            replaced = re.sub('\\b'+ pattern +'\\b',  color(pattern, color_), new)
            new = replaced

    else:
        pattern = (syntax[key])
        color_ = int(theme[key])
        match = re.findall(pattern , new, re.DOTALL)

        print(match)

        '''
        for j in match:
            replaced = re.sub(j,  color(j, fg=color_), new)#(new.replace(i, color(i, fg=color_)))
            new = replaced
        '''


"""

dette er en comment

python.syntax python.theme rpn.py

"""

