def mid(x,y,z):
    '''返回由小到大三个值'''
    if x > y:
        temp = x
        x = y
        y = temp
    if y > z:
        temp = y
        y = z
        z = temp
    if x > y:
        temp = x
        x = y
        y = temp
    return x, y, z

a, b, c = map(int,input().split())
a, b, c = mid(a,b,c)
if a + b <= c:
    print("Not triangle")
    exit()
if a ** 2 + b ** 2 > c ** 2:
    print("Acute triangle")
if a ** 2 + b ** 2 == c ** 2:
    print("Right triangle")
if a ** 2 + b ** 2 < c ** 2:
    print("Obtuse triangle")
if a == b:
    print("Isosceles triangle")
if a == b == c:
    print("Equilateral triangle")
