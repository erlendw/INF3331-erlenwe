import sys
syspath = sys.path[0] + "/"

args = sys.argv

args.pop(0)

highlightfile_old = syspath + args[0]
highlightfile_new = syspath + args[1]

with open(highlightfile_old) as data:
    original = data.readlines()

with open(highlightfile_new) as data:
    modified = data.readlines()


matrix = []

for i in range(len(original) + 1):
    row = []
    for j in range(len(modified) + 1):
        row.append(0)
    matrix.append(row)


for i in range(1, len(original)+1):
        for j in range(1, len(modified)+1):
            if original[i-1] == modified[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                if matrix[i][j-1] > matrix[i-1][j]:
                    matrix[i][j] = matrix[i][j-1]
                else:
                    matrix[i][j] = matrix[i-1][j]

print(matrix)

output = open('out.txt','w')

def print_result(matrix, org, mod, i, j,output):

    if i > 0 and j > 0 and org[i-1] == mod[j-1]:
        print_result(matrix, org, mod, i-1, j-1, output)
        if i == len(org):
            output.write("0" + org[i-1] + "\n")
        else:
            output.write("0" + org[i-1])

    else:
        if j > 0 and (i == 0 or matrix[i][j-1] >= matrix[i-1][j]):
            print_result(matrix, org, mod, i, j-1, output)
            if j == len(mod):
                output.write("+" + mod[j-1] + "\n")
            else:
                output.write("+" + mod[j-1])


        elif i > 0 and (j == 0 or matrix[i][j-1] < matrix[i-1][j]):
            print_result(matrix, org, mod, i-1, j, output)
            if i == len(org):
                output.write("-" + org[i-1] + "\n")
            else:
                output.write("-" + org[i-1])

print_result(matrix, original, modified, len(original), len(modified), output)

output.close()