a = input()
b = input()
if "@" in a:
    print("Некорректный логин")
elif "@" in b:
    print("OK")
else:
    print("Некорректный адрес")
