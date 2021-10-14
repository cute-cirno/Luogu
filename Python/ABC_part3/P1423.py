count = 1
distance = float(input())
init = 2
swimming = 2
while swimming < distance:
    count +=1
    init = init*0.98
    swimming +=init
print(count)