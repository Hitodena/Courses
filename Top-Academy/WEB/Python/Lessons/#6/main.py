# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []

# c = a + b
# print(c)

# if len(b) > len(a):
#     for i in range(len(a)): # 0 - 3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)): # range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)


# if len(b) > len(a):
#     a, b = a, b
# for i in range(len(a)): # 0 - 3
#         c.append(a[i])
#         c.append(b[i])
# for i in range(len(a), len(b)): # range(3, 5)
#         c.append(b[i])
# print(c)





# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# # a.remove(3) # удаление по значению
# # print(a)
# n = 52
# # if n in a:
#     # a.remove(n) # ошибка value error если значения нет
# last = a.pop() # удаляет последний элемент
# print(last)
# print(a)
# second = a.pop(1) # по индексу
# print(second)
# print(a)
# a.clear() # полная очистка списка
# print(a)




# n = [int(input("-> ")) for i in range(int(input("-> ")))]
# print(n)
# k = int(input("Введите индекс: "))
# n.pop(k)
# print(n)




# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# num = a.count(5) # возвращает кол-во заданных значений в списке
# print(num)
# ind = a.index(3) # возвращает индекс текущего элемента, несколько - первая по счёту; второе значение - с какого начинать 
# print(ind)
# a.reverse() # реверс списка
# print(a)
# a.sort() # сортировка (по умолчанию - по возрастанию)
# print(a)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(reverse=True, key=len) # не по а-я, а по я-а, len - по длине слов
# print(s)



# s = [1, 5, 3, 2, 3, 4, 3, 5]
# print(s)
# # s.sort()
# print(sorted(s, reverse=True)) # возвращает новый список
# print(s)



# a = [1, 2, 3]
# b = a.copy()
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# b.append(120)
# print("a =", a, id(a))
# print("b =", b, id(b))




import random as r 

# print(r.random())
# print(r.randint(0, 9)) # от 0 - 9 включительно
# print(r.randrange(2, 9, 2)) # start stop step
# print(round(r.uniform(10.5, 25.5), 2))

# city_list = ["Москва", "Сочи", "Урюпинск", "Калининград"]
# print(r.choice(city_list))
# print(r.choices(city_list, k=3))

# s = [20, 30, 40, 50, 60, 70, 80, 90]
# print(r.choice(s))
# print(r.choices(s, k=3))
# r.shuffle(s) # перемешка
# print(s)


# array = ["a", "b", "c"]
# array = [r.randint(0, 100) for i in range(r.randint(0,100))]
# print(array)
# print(len(array))
# print(min(array))
# print(max(array))
# print(sum(array))

# s = 0
# for i in range(len(array)):
#     s += array[i]
# print(s)


# array = [r.randint(0, 100) for i in range(10)]
# print(array)
# m = max(array)
# print("Max:", m)
# array.remove(m)
# array.insert(0, m)
# print(array)


# array.sort(reverse=True)
# print(array)

array = [r.randint(-20, 20) for i in range(20)]
print(array)
mi = min(array)
minindex = array.index(mi)
print("Min:", mi)
print("Min index:", minindex)
print(array[minindex:])
