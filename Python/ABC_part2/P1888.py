import math
a = input().split()
def hcf(x, y):
   if x > y:
       smaller = y
   else:
       smaller = x
       
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i
   return hcf

b = []
for i in a:
    b.append(int(i))
c = min(b)
d = max(b)
e = hcf(c,d)
print("{}/{}".format(int(c/e),int(d/e)))