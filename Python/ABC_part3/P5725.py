n = int(input())
s = []
for i in range(n**2+1):
    s.append(i)
count = 1
for i in range(n):
    for j in range(n):
        print("{:02d}".format(s[count]),end='')
        count += 1
    print()
count = 1
for i in range(n+1):
    for k in range(n-i):
            print("  ",end='')
    for j in range(i):
        print("{:02d}".format(s[count]),end='')
        count += 1
    print()