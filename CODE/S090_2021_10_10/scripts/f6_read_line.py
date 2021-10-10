
with open('file4.txt', 'r') as f:

    while True:
        data = f.readline()
        if data == '':
            break
        print(len(data), repr(data))
