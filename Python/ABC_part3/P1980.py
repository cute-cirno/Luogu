a, b = map(int,input().split())
ch = str(b)
s = [""]
count = 0
for i in range(1,a+1):
    s.append(str(i))
for j in s:
    for k in j:
        if k == ch:
            count += 1
print(count)
