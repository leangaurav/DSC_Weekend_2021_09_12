
with open('file4.txt', 'r') as f:

    while True:
        data = f.read(10)
        if data == '':
            break
        print(len(data), repr(data))
