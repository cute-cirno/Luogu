import math

n = int(input())
s5 = math.sqrt(5)
Fn = ((1+s5) ** n - (1-s5) ** n) / (2 ** n * s5)
print("{:.2f}".format(Fn))