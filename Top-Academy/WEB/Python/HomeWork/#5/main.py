s = []
n = int(input("Кол-во чисел -> "))
for i in range(n):
    x = int(input("Число -> "))
    if x % 3 == 0:
        s.append(x)
    else:
        print(x, "не делится на 3 без остатка")
print(s)