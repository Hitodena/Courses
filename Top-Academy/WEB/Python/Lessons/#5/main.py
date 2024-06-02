# a = [int(input("-> ")) for i in range(int(input("n = ")))] #type: ignore
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print(s)



# lst = list(range(10, 100, 10))
# print(lst)
# # for i in lst:
# #     print(i, end=" ") # мы сразу в списке
# # for i in range(len(lst)):
# #     print(i, end=" ") # i - количество итераций
# for i in range(len(lst)):
#     print(lst[i], end=" ") # i - индекс листа



# colors = ["red", "blue", "green"]
# for i in range(len(colors)):
#     print(colors[i], end=" ")



# count = s = 0
# array = list(range(21, 41))
# print(array)
# # for i in array:
# #     if i % 2 == 0: 
# #         count += 1
# # for i in range(len(array)):
# #     if array[i] % 2 != 0:
# #         s += array[i]
# for i in array:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print(count, s, end="    ")


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# for i in a:
#     if i > i - 1:        # здесь так не получится
#         print(i, end=" ")


# a = [7, 9, 3, 1, 2]
# print(a)
# a[1], a[0] = a[0], a[1]
# print(a)



# Срезы - список [start:stop:step]

# lst = [6, 9, 3, 7, 1, 8]
# print(lst[5:0:-1])   # 1 - start  2 - end not include
# i = 5
# while i > 0:
#     print(lst[i])
#     i -= 1
# print(lst[10]) # не работает

# print(lst, id(lst))
# b = lst[5:16] # работает
# print(b, id(b))


# s = "Hello World"
# print(s[6:])


# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:7])
# print(s[4:1:-1])
# print(s[2:5])



# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2] = 56
# print(s)

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:5] = []
# print(s)
# del s[1:3]
# print(s)



# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# # s[len(s):] = [12]
# s.append(12) # один элемент в конец спика
# print(s)
# s.extend([1, 2, 3]) # любое кол-во элементов в конец списка
# print(s)
# s.extend("add")
# print(s)
# s.insert(-1, "Hello") # добавляет элемент в заданный индекс, а остальное сдвигает  ()
# print(s)
# # s.insert(20, 90) # не рекомендуется
# # print(s)



# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)


a = [5, 9, 2, 1, 4, 3]
b = [4, 2, 1, 3, 7]
c = [] # [2, 1, 4, 3]
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
for element in a:
    if element not in c and element in b:
        c.append(element)
print(c)


