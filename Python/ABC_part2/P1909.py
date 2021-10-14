import math
x = int(input())
n = []
sum = []
for i in range(3):
    n.append(input().split())
    sum.append(math.ceil(x / int(n[i][0])) * int(n[i][1]))
print(min(sum))