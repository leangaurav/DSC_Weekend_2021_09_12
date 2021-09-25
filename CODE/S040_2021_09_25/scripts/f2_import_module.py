# D:\DATA\Desktop\tutort\DSC_Weekend_2021_09_12\CODE\S040_2021_09_25\scripts
# 1
print()
import random
print(random.randrange(10)) # 0 - (n-1)
print(random.randrange(10,20)) # 10 - 19
print(random.randrange(10,20,2)) # 10, 12 ,14, 16, 18

# 2
print()
import random as rr # alias
# import numpy as np
print(rr.randrange(10))

# 1 and 2 are equivalent

# 3
print()
from random import randrange, uniform
print("randrange(10)", randrange(10))
print("uniform", uniform(10,20))  # floating number in the range

# 4
print()
from random import randrange as rd
print(rd(10,20))

# 5 : worst option
print()
from random import * # import everything from the module
print("randrange(10)", randrange(10, 20)) # 10 - 19
print("randint", randint(10,20))  # 10 - 20
