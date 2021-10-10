
f = open('file2.txt', 'w')
print("closed", f.closed)
f.write("hello from python")

f.close()
print("closed", f.closed)

# f.write("after closed")
