a = float(input())
b = float(input())
opr = input()
if opr in '+-*/':
    if opr == '+':
        print(a + b)
    elif opr == '-':
        print(a - b)
    elif opr == '*':
        print(a * b)
    else:
        if b == 0:
            print('888888')
        else:
            print(a / b)
else:
    print('888888')
