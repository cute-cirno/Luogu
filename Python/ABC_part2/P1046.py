def canPick(apple,person):
    if apple > person+30:
        return False
    else:
        return True
a = list(map(int,input().split()))
b = int(input())
sum = 0
for i in a:
    if canPick(i,b):
        sum += 1
print(sum)