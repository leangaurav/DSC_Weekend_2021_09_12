
# context handler
with open('file3.txt', 'w') as f:
  f.write("hello from python")
  print("closed", f.closed)

print("closed", f.closed)
