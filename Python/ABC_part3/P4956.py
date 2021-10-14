n = int(input())
per = n / 52
k = 1
if per < 21:
    print(0)
    print(1)
    exit()
if per < 28:
    print(1)
    print(1)
while True:
    flag = 0
    for i in range(101):
        if k * 21 + 7 * i == per:
            print(i)
            print(k)
            flag = 1
    k += 1
    if flag == 1:
        break