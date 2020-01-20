import sys

args = sys.argv

file_name = args[1]

f = open(file_name)
line = f.readline()
while line:
    print("\"{}\",".format(line.replace("\n", "")))
    line = f.readline()
f.close()
