
with open('file4.txt', 'r') as f:
    print("before reading once", f.tell())
    data = f.read()
    print(repr(data))
    print(type(data))

    print("after reading once", f.tell())
    print()
    print("reading second time")
    data = f.read()
    print(repr(data))

    print()
    f.seek(10)
    print("after pointer reset", f.tell())

    print()
    print("reading after ")
    data = f.read()
    print(repr(data))
