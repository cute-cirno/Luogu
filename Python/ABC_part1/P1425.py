s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])
if d < b:
    f = d + 60 - b
    e = c - 1 - a
else:
    f = d - b
    e = c - a
print("%d %d"%(e,f))