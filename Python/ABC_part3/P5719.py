n, k = map(int, input().split())
a = []
b = []
for i in range(1,n+1):
    if i % k == 0:
        a.append(i)
    else:
        b.append(i)

c = sum(a)/len(a)
d = sum(b)/len(b)
print("{:.1f} {:.1f}".format(c,d))