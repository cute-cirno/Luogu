n = int(input())
a = input().split()
max = 0
count = 0
for i in range(n-1):
    if int(a[i]) + 1 == int(a[i+1]):
        count += 1
        if count > max:
            max = count
    else:
        count = 0
print(max+1)