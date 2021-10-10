import sys

print(sys.argv)
f_name = sys.argv[0]

with open(f_name, 'r') as f:
  print(f.read())
