a = float(input())
if (a <= 0.000001 and a >= -0.000001) or a == 0:
    print(1000000)
else:
    print(1 / a)
