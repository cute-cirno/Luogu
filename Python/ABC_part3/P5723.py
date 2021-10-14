import math

def prime(x):
    '''if x is a prime number, function will retuen it, if not, return 0'''
    if x == 2:
        return x
    flag = 1
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            flag = 0
            break
    if flag == 1:
        return x
    else:
        return 0

l = int(input())
a= []
sum = 0
count = 0
for i in range(2,100000):
    if not prime(i) == 0:
        a.append(i)
        sum += i
        count +=1
    if sum > l:
        del(a[-1])
        count -= 1
        break
for j in a:
    print(j)
print(count)