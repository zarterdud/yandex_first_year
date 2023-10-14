a = input()
b = input()
c = 'Тула'
x = 'Пенза'
if a == b:
    print('НЕТ')
elif (a == c) and (b == x) or (a == x) and (b == c):
    print('НЕТ')
elif (a == c) and (b == c) or (a == x) and (b == x):
    print('НЕТ')
elif (a != c) and (a != x) and (b != c) and (b != x):
    print('НЕТ')
elif (a == x) or (b == c):
    print("НЕТ")
else:
    print('ДА')
