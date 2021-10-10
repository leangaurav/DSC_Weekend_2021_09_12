
with open('file4.txt', 'r') as f:
    for data in f:
        print(len(data), repr(data))

print()

with open('file4.txt', 'r') as f:
    data = f.readlines()
    print(data)
