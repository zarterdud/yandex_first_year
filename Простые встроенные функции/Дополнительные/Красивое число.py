a = int(input())
q = a // 100 % 100
w = a // 10 % 10
e = a % 10
c = [q, w, e]
if (max(c) + min(c)) / 2 == (q + w + e) - (max(c) + min(c)):
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')
