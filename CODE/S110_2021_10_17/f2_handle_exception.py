

def f():
    x = int(input("Enter a  value:"))
    if x == 0:
        exit()
    else:
        raise  ValueError(x)

print("before")

try:
    f()
except Exception as err:
    print("handled an error", err)
print("after")
