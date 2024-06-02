# d = {"x1": 3, "x2": 7, "x3": [5, 6], "x4": -1}
# print(len(d))


# goods = {
#     "1": ["Core-13-4330", 9, 4500], 
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400]
# }

# for key in goods:
#     print(key, ")" , goods[key][0], " - ", goods[key][1], "шт. по ", goods[key][2], "руб.", sep="")

# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение неккоректно")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break

# for key in goods:
#     print(key, ")" , goods[key][0], " - ", goods[key][1], "шт. по ", goods[key][2], "руб.", sep="")



# d = {"x1": 3, "x2": 7, "x3": 5}
# print(d)
# # del(d["x1"])
# # d["x4"] = 10
# # print(d)
# # a = {"one": 1}
# print(d.values())
# print(d.keys())
# print(d.items())
# # for key, value in d.items():
# #     print(key, "->", value)
# print(list(d))
# print(list(d.values()))
# print(list(d.items()))


# d = {"x1": 3, "x2": 7, "x3": 5}

# d2 = d
# print("d = ", d)
# print("d2 = ", d2)
# d2["x4"] = 18
# print("d = ", d)
# print("d2 = ", d2)


# d = {"x1": 3, "x2": 7, "x3": 5}
# print(d)
# # value = d.get("x4", "Такого ключа не существует")
# # print(value)
# item = d.pop("x1")
# print(item)
# print(d)
# d.clear()
# print(d)



# d = {"x1": 3, "x2": 7, "x3": 5}
# print(d)
# item = d.setdefault("x1", 10)
# print(item)
# print(d)
# a = {"one": 1, "two": 2, "x1": 10}
# d.update(a)
# print(d)

# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# z = x | y
# # z = x.copy()
# # z.update(y)
# print(z)

# d = dict.fromkeys(["a", "b", "c"], 100)
# print(d)


# emp = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New York"
# }

# emplf = dict()
# emplf["name"] = emp.pop("name")
# emplf["salary"] = emp.pop("salary")
# print(emp)
# print(emplf)

# emp = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New York"
# }

# emp["location"] = emp.pop("city")
# print(emp)


# d = {
#     "first" : {
#         1: {
#             11: "abc"
#         },
#         2: {
#             11: "abc"
#         },
#         3:{
#             11: "abc"
#         }
#     },
#     "second" : {
#         4: {
#             11: "abc"
#         },
#         5: {
#             11: "abc"
#         }
#     }
# }

# print(d)

# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ":", d[x][y])
#         for z in d[x][y]:
#             print("\t\t", z, ":", d[x][y][z])



# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# d2 = {key: value for key, value in d.items()}
# print(d2)
# d2 = {value: key for key, value in d.items()}
# print(d2)
# d2[1], d2[4] = d2[4], d2[1]
# print(d2)


array = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -28]

d = {}
s = None

for i in array:
    if type(i) == str:
        d[i] = []
        s = i
    else:
        d[s].append(i)


print(d)



