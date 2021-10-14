import math
s, v = map(int,input().split())
hh, mm = 7, 50
hh = 7 - int(s/v/60)
mm = 50 - math.ceil(s/v%60)
if(hh<0):
    hh = 24 + hh
if(mm<0):
    mm = 60 + mm
    hh -= 1
print("{:02d}:{:02d}".format(hh,mm))