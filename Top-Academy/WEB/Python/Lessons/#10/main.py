# s = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # a = [x for x in s if "a" not in x]
# # a = ['A' + x[1:] if x[0] == 'a' else 'B' + x[1:] for x in s if x[1] == "c"]
# a = {'A' + x[1:] if x[0] == 'a' else 'B' + x[1:] for x in s if x[1] == "c"}
# print(a)

# # тернарное выражение q = True if condition

# for x in s:
#     if x[1] == "c":
#         if x[0] == "a":
#             print("A" + x[1:])
#         else:
#             print("B" + x[1:])



# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a | b
# c |= a | b
# c = a.union(b)
# print(c)

# c = a & b
# print(c)

# a &= b
# print(a)

# c = a - b # уникальный из первого, но из второго не возвращает
# print(c)

# c = a ^ b
# print(c)



# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}

# su = s1.union(s2, s3, s4, s5, s6, s7)
# # su = s1|s2|s3|s4|s5|s6|s7

# print(su)
# print(f"Unic elements: {len(su)}")
# print(f"min: {min(su)}")
# print(f"max: {max(su)}")



# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# s = set(a) & set(b)
# print(s)
# for i in s:
#     print(i, end=" ")


# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# s = set(a) - set(b)
# print(s)
# for i in s:
#     print(i, end=" ")



# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}

# print(f"One hobby: {drawing ^ music}")
# print(f"Both hobby: {drawing & music}")

# drawing = drawing - music
# print(drawing)




# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a < b)



# frozenset

# s = frozenset([1, 2, 3 ,4 ,5 ,6])
# print(s)
# s = frozenset("Hello")
# print(s)


# словари (dict)

# s = [1, 2, 3]
# d = {"one" : 1,
#      "two": 2,
#      "three" : 3}
# print(s[1])
# print(d["two"])

# d = {0: "test", "one": 45, (1, 2.3): "Кортеж", True: 1} # не может иметь в виде ключей изменяемые виды данных, ключи меняться не могут
# print(d)

# d[(1, 2.3)] = 100
# print(d) 



# d = {"one": 1, "two": 2}
# print(d)
# print(type(d))

# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d))



# d1 = dict(["one", 1, "two", 2])
# d1 = dict({("one", 1), ("two", 2)})
# d1 = dict(["on", ("two", 2)])
# print(d1)



# d = {x: x ** 2 for x in range(7)}
# print(d)


# d = {"one": 1, "two": 2, "three": 3}
# # print("two" in d)
# # print(len(d))
# # for key in d:
# #     print(key, "->", d[key])
# key = "one"
# del d[key]
# print(d[key])
# if key in d:
#     print(d[key])
# try:
#     print(d[key])
# except KeyError:
#     print("такого ключа нет")
# print(d)


# m = 1
# dc = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# for key in dc:
#     m *= dc[key]
# print(m)



# dt = dict()
# dt[1] = input("--> ")
# dt[2] = input("--> ")
# dt[3] = input("--> ")
# dt[4] = input("--> ")
dt = {key: input("--> ") for key in range(int(input("---> ")))}
print(dt)
try:
    disLike = int(input("Какой элемент исключить: "))
    del dt[disLike]
except (KeyError, ValueError):
    print("Такого ключа не существует")
print(dt)