# WAFs
# area_circle(r)
# area_square(s)
# area_rect(l,b)

def area_circle(r):
    return 3.14*r*r
def area_square(s):
    return s*s
def area_rect(l,b):
    return l*b

if __name__ == '__main__':
    print("area_circle is :- ", area_circle(5))
    print("area_square is :- ", area_square(5))
    print("area_rect is :- ", area_rect(2,3))
