import sys
with open(sys.argv[1]) as filename:
    count = 0
    for line in filename:
        count = count + line.count(' ')
print(count)