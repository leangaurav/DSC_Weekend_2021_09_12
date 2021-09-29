import sys

if len(sys.argv) != 3:
    print("Invalid input. Pass two numbers")
    exit()

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

print(n1 + n2)
