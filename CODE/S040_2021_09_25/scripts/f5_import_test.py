import test

print(test.a)
print("f5", __name__)

from test import a
print("f5", a)
