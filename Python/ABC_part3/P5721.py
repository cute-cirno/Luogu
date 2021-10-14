n = int(input())
new = 0
for i in range(n,0,-1):
    for j in range(i):
        new += 1
        print("{:02d}".format(new),end='')
    print()