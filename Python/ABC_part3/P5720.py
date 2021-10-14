a = int(input())
if a == 1:
    print(1)
    exit()
for i in range(2,100000,1):
    a >>= 1
    # print(i,end=' num:')
    # print(a)
    if a == 1:
        break
print(i)