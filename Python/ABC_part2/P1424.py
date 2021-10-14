a = [1,1,1,1,1,0,0]
x, n =map(int,(input().split()))
fullWeek = int(n/7)
day = n % 7 
sum = fullWeek * 1250
if x + day <= 8:
    for i in a[x-1:x+day-1]:
        if i:
            sum += 250
else:
    for i in a[x-1:7]:
        if i:
            sum += 250
    for i in a[0:day+x-8]:
        if i:
            sum += 250
print(sum)