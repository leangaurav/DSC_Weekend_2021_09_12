
# python f3_assert.py # debug mode True
# python -O f3_assert.py # debug mode False -> assert statements are skipped
x = int(input("enter a number"))
print("debug", __debug__)
assert x==0, "not zero"
