a, b, c = map(int,(input().split()))
if(a>b):
    temp = a
    a = b
    b = temp
if(b>c):
    temp = b
    b = c
    c = temp
if(a>b):
    temp = b
    b = a
    a = temp
print("{} {} {}".format(a,b,c))
