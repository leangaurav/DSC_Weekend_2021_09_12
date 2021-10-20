import sys
from string import printable
with open(sys.argv[1]) as file:
    data = file.read()
    for c in printable:
        if c in data:
            print(repr(c), data.count(c))