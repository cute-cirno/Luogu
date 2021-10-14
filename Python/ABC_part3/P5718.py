n = input()
a = input().split()
min = int(a[0])
for i in a:
    if int(i) < min:
        min = int(i)
print(min)