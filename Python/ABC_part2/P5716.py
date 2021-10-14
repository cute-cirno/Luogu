yy, mm = map(int,(input().split()))
if yy % 400 == 0:
    flag = 1
elif yy % 4 == 0 and not yy % 100 == 0:
    flag = 1
else:
    flag = 0
big = [1,3,5,7,8,10,12]
if mm in big:
    print(31)
elif mm == 2:
    if flag == 0:
        print(28)
    else:
        print(29)
else:
    print(30)
