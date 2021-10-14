x = int(input())
localTime =  5 * x
luoguTime = 11 + 3 * x
if(localTime < luoguTime):
    print("Local")
else:
    print("Luogu")