
with open("file9.txt", 'w') as f:
  f.write("line1")
  f.flush()

  input("after line1")
  print("line2", file=f, flush=True)

  input("after line2")
  f.write("line3")

input("after closing")
