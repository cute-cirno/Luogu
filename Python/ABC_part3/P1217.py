import math

ar = [5,7,11]

for i in range(1, 10, 2):  # 3
    for j in range(10):
        palindrome = 100*i + 10*j + i
        ar.append(palindrome)

for i in range(1, 10, 2):  # 5
    for j in range(10):
        for k in range(10):
            palindrome = 10000*i + 1000*j + 100*k + 10*j + i
            ar.append(palindrome)


for i in range(1, 10, 2):  # 7
    for j in range(10):
        for k in range(10):
            for l in range(10):
                palindrome = 1000000*i + 100000*j + 10000*k + 1000*l + 100*k + 10*j + i
                ar.append(palindrome)

def prime(x):
    '''if x is a prime number, function will retuen it, if not, return 0'''
    if x == 2:
        return True
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return 0
    return True

def palin(x):
    '''judge a number is or isn't a palindrome number'''
    c = str(x)
    if c == c[::-1]:
        return True
    return False

a, b = map(int,input().split())
if b>100000000:
    b=100000000
for i in ar:
    if i <= b and i >= a and prime(i) and palin(i):
        print(i)