x = int(input())
if x <= 150:
    y = 0.4463 * x
    pass
elif x <= 400:
    y = 66.945+0.4663*(x-150)
    pass
else:
    y = 183.52 + (x-400)*0.5663
    pass
print("{:.1f}".format(y))