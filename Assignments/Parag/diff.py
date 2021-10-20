import sys
import filecmp

def filecompare(f1,f2):
    result = filecmp.cmp(f1, f2)
    print(result)

file1 = sys.argv[1]
file2 = sys.argv[2]
filecompare(file1, file2)