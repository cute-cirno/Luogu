storage = 0
budget = []
balance = 0
flag = False
for i in range(12):
    budget.append(int(input()))
for i in range(12):
    balance += 300
    balance -= budget[i]
    if balance < 0:
        print(0-(i+1))
        flag = True
        break
    a = balance%100
    if a:
        storage += a*100
        balance -= a*100