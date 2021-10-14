a = int(input())
if(a%2 == 0 and a>4 and a <=12):
    print("1",end=" ")
else:
    print("0",end=" ")

if(a%2 == 0 or a > 4 and a <= 12):
    print("1",end=" ")
else:
    print("0",end=" ")

if  (a%2 == 0 and not(a>4 and a <=12) 
    or not a%2 == 0 and a > 4 and a <= 12):
    print("1",end=" ")
else:
    print("0",end=" ")
if(not a%2 == 0 and not (a>4 and a <=12)):
    print("1",end="")
else:
    print("0",end="")