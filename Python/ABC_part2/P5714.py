m, h = map(float,(input().split()))
alpha = m / h ** 2
if(alpha<18.5):
    print("Underweight")
elif(alpha<24):
    print("Normal")
else:
    print("{:.6g}".format(alpha))
    print("Overweight")