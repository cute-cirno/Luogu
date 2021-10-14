import math
m, t, s=map(int,input().split())
if t == 0:
    print(0)
elif int(m-s/t) <= 0:
    print(0)
else:
    print(int(m-s/t))