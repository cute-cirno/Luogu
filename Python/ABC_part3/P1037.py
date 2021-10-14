def cutZero(s):
    nums = []
    for i in s:
        nums.append(i)
    while nums[0] == '0':
        del(nums[0])
    if nums[-1] == '-':
        del nums[-1]
    return nums


a = input()
num = int(a)
if num == 0:
    print(0)
elif num > 0:
    s = a[::-1]
    new = cutZero(s)
    for i in new:
        print(i, end='')
else:
    s = a[::-1]
    new = cutZero(s)
    print('-',end='')
    for i in new:
        print(i, end='')
