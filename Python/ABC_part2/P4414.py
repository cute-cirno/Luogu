def mid(x,y,z):
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
A, B, C = mid(a,b,c)
string = input()
for i in string:
    if i == 'A':
        print(A,end='')
    elif i == 'B':
        print(B,end='')
    elif i == 'C':
        print(C,end='')
    if not i == string[2]:
        print(end=' ')