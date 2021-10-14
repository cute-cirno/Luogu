sumtime = []
for i in range(7):
    a, b = map(int, input().split())
    sumtime.append(a + b)
maxtime = 0
for index, i in enumerate(sumtime):
    if i > 8 and i > maxtime:
        maxtime = i
        maxindex = index
if maxtime == 0:
    print(0)
else:
    print(maxindex+1)