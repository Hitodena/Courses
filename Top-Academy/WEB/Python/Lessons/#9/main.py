# s = tuple(i for i in range(5))
# s = tuple(input("-> " for i in range(5)))
# print(s)

# s = tuple(2**i for i in range(1, 13))
# print(s)


# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3.count("l"))
# print(t3.count("a"))
# # print(t3.index("l", 4))
# ch = "w"
# try:
#     print(t3.index(12312))
# except ValueError:
#     print("ADSDSAD")




# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()


# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# import random as r

# def fill(start, end): 
#     tup = tuple(r.randint(start, end + 1) for i in range(10))
#     return tup


# tpl1 = fill(3, 5)
# print(tpl1)
# tpl2 = fill(-5, 8)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3, "\n", tpl3.count(0))




# t = (10, 11, [1, 2, 3], [4, 5 ,6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))



# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t # распаковка кортежа
# print(x, y, z)



# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married

# # user = get_user()
# # print(user)
# first_name, year, married = get_user()
# print(first_name, year, married)
# # print(user[0])
# # print(user[1])
# # print(user[2])




# def func(lst):
#     return(sum(lst), len(lst))


# a, b = func([2, 9, 6, 5, 8, 7, 5, 8, 7, 1, 4, 5, 4])
# print("Сумма:", a)
# print("Количество:", b)



# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst = list(tpl)
# print(lst)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country    
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")




# Множества (set)



# s = {"banana", "apple", "orange", "banana", "apple", "orange"}
# print(s, type(s), len(s))
# for i in s:
#     print(i)


# a = set("Hello")
# print(type(a))
# print(a)


# s = {i * i for i in range(10)}
# print(s)


a = set("hello")
print(a)
print("a" in a)
a.add("a")
print(a)
el = "o"
if el in a:
    a.remove(el)
a.pop()
a.discard("o")
print(a)