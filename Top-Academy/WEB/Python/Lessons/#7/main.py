# lst = []
# # if len(lst) == 0:
# if not lst:
#     print("Списокы пустой")

from random import randint

# n1 = int(input("Количествово элементов в первом списке -> "))
# n2 = int(input("Количествово элементов во втором списке -> "))
# array = [randint(0, 10) for i in range(n1)]
# arraysec = [randint(0, 10) for i in range(n2)]
# print("Первый список:", array)
# print("Второй список:", arraysec, "\n")

# arrayth = array + arraysec
# print("Третий список(сумма обоих):", arrayth, "\n")


# arrayth = []
# for i in range(len(array)):
#     if array[i] not in arrayth:
#         arrayth.append(array[i])
# for i in range(len(arraysec)):
#     if arraysec[i] not in arrayth:
#         arrayth.append(arraysec[i])
# print("Третий список(перебор от дубликатов): ", arrayth, "\n")


# arrayth = []
# for i in range(len(array)):
#     if array[i] in arraysec and array[i] not in arrayth:
#         arrayth.append(array[i])
# print("Третий список(дубликаты): ", arrayth, "\n")


# arrayth = [min(array), min(arraysec), max(array), max(arraysec)]
# print("Третий список(макс/мин значения): ", arrayth)






# Матрицы

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()


# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()



# w, h = 5, 3
# matrix = [[0 for x in range(w)]for y in range(h)]
# a = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)

# print(matrix)



# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(f"{x} + {y} = {x + y}")



# w, h = 5, 3
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# print(matrix)
# count = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             count += 1
#     print()
# print("Количество отрицательных элементов:", count)






# Modules

import math as m

# r = int(input("Введите радиус окружности: "))
# print("Длинна окружности: ", round(2 * m.pi * r, 2))


# a = int(input("1 катет: "))
# b = int(input("2 катет: "))
# c = m.sqrt(a ** 2 + b ** 2)
# print(round(c, 0))


import time as t
import locale
# seconds = t.ctime()
# res = t.localtime()
# print(seconds)
# print(res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")

# print(t.strftime("Today is %b %d %Y"))
# print(t.strftime("%d/%m/Y, %H:%M:S"))


# locale.setlocale(locale.LC_ALL, "ru")
# print(t.strftime("Сегодня %B %d, %Y"))


# start = t.monotonic()
# t.sleep(5)
# finish = t.monotonic()
# res = finish - start
# print(res)



# func



# def hello(name):
#     print("Hello", name)


# hello("Irishka")


def get_sum(a, b):
    print(a + b)


x = 2
y = 5
get_sum(x, y)
n = 6
m = 3
get_sum(n, m)
get_sum("abc", "def")


