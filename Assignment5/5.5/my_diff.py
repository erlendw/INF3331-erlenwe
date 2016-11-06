import sys
import json
import re
from colors import color

syspath = sys.path[0] + "/"

args = sys.argv

args.pop(0)

highlightfile_old = syspath + args[0]
highlightfile_new = syspath + args[1]

with open(highlightfile_old) as data:
    original = data.readlines()

with open(highlightfile_new) as data:
    modified = data.readlines()

modified_length = len(modified)
original_length = len(original)


diff = modified_length -original_length


if(diff < 0):
    lines = original_length
else:
    lines = modified_length

i = 0
j = 0

output = ""

while(True):

    if(i >= original_length):
        while(j < modified_length):
            output +=("+ " + modified[j])
            j += 1
        break

    if(j >= modified_length):
        while(i < original_length):
            output +=("- " + original[i])
        break


    if(original[i] == modified[j]):
        output +=("1 0 " + original[i])

    elif original[i+1] == modified[j+1]:
        output +=("2-" + original[i])
        output +=("2+" + modified[j])

    elif original[i] == modified[j+1]:
        output +=("3+" + modified[j])
        j+=1

    elif original[i+1] == modified[j]:
        output +=("4-" + original[i])
        j-=1

    i+=1
    j+=1

print(output)