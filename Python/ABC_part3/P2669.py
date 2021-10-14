k = 200
a = []
for i in range(1,k):
    for j in range(i):
        a.append(i)
        if len(a) > 10000:
            break
n = int(input())
sum = 0
for i in range(n):
    sum += a[i]
print(sum)