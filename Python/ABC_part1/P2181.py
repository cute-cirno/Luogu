from decimal import *
n = int(input())
a = n*(n-1)*(n-2)*(n-3)
print(Decimal(a) / Decimal(24))