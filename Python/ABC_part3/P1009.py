def fib(x):
    s = 1
    for i in range(1,x+1):
        s *= i
    return s

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += fib(i)
print(sum)