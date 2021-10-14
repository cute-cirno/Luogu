flag = 1
year = int(input())
if(year % 400 == 0):
    flag = 1
elif(year % 4 == 0 and not year % 100 == 0):
    flag = 1
else:
    flag = 0
print(flag)