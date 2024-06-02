from random import randint

array = [randint(0, 100) for i in range(randint(0, 20))]
print(array)


c = int(input("Введите число: "))
k = int(input("Введите индекс: "))

array.insert(k, c)
print(array)
