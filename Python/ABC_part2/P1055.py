import re
flag = 0
isbn = input()
n = []
sum = 0
for i in range(13):
    ch = re.search(
    "(\d)(-)(\d)(\d)(\d)(-)(\d)(\d)(\d)(\d)(\d)(-)(.)",isbn
    ).group(i+1)
    if not ch == '-':
        if not ch == 'X':
            n.append(int(ch))
        else:
            n.append(ch)
            flag = 1

for i in range(9):
        sum += n[i] * (i+1)

d = sum % 11

if d == n[9] or d == 10 and n[9] == 'X':
    print("Right",end='')
elif d == 10:
    reIsbn = isbn[:12] + 'X'
    print(reIsbn,end='')
else:
    reIsbn = isbn[:12] + str(d)
    print(reIsbn,end='')