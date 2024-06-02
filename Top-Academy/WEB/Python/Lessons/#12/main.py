# # zip ()

# # one = [1, 2, 3, 4, 5]
# # two = ["one", "two", "three"]

# # d = dict(zip(one, two)) # one - keys, two - arguments
# # print(d)

# # lst = list(zip(one, two)) # One - two, one - two
# # lst = list(zip(one))
# # print(lst)

# # f = {k: v for k, v in zip(one, two)}
# # print(f)



# # one = {"name": "Igor", "surname": "Doe", "job": "Consultant"}
# # two = {"name": "Irina", "surname": "Smith", "job": "Manager"}
# # three = {"name": "Irina", "surname": "Smith", "job": "Manager"}


# # for (k1, v1), (k2, v2), (k3, v3)  in zip(one.items(), two.items(), three.items()):
# #     print(k1, "->", v1)
# #     print(k2, "->", v2)
# #     print(k3, "->", v3)



# # lst = [(1, "one"), (2, "two"), (3, "three")]
# # a, b = zip(*lst)
# # print(a)
# # print(b)


# # a = {"one": 1, "two": 2}
# # b = {"three": 3, "four": 4}
# # print({**a, **b})

# # for k, v in {**a, **b}.items():
# #     print(k, "->", v)


# # data = ["red", "green", "blue"]

# # # data = [5, 7, 9, 4, 1, 3, 5, 8, 6, 4]
# # # j = 1
# # # for i in data:
# # #     print(j, ")", i, sep="")
# # #     j += 1
# # for num, color in enumerate(data, 1):
# #     print(num, ")", color, sep="")


# # a = [1, 2, 3]
# # b = [*a, 4, 5, 6]
# # print(b)


# # def func(*args):
# #     return(args)


# # print(func(5))
# # print(func(5, 6, 7, "abc"))
# # print(func())


# # def summa(*param):
# #     res = 0
# #     for i in param:
# #         res += i
# #     return(res)


# # print(summa(123123123123,1,23123123,12312,32,13,12,5,21,4,12,1,23,12))



# # def to_dict(*args):
# #     # d = {}
# #     # for i in args:
# #     #     d.update({i: i})
# #     # return(d)
# #     return{i: i for i in args}
        

# # print(to_dict(1, 2, 3, 4, 5, "grey"))




# # def func(*args):
# #     avg = sum(args) / len(args)
# #     print(avg)
# #     res = []
# #     for num in args:
# #         if avg > num:
# #             res.append(num)
# #     return(res)



# # def func(a, *args):
# #     return(a, args)


# # print(func(1,))

# # print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# # print(func(3, 6, 1 ,9 ,5))



# # def print_scores(student, *scores):
# #     print("Name:", student)
# #     for score in scores:
# #         print(score, end=" ")


# # print_scores("Jenya Shina", 5, 4, 5, 3, 5, 5, 5, 5, 5, 5)



# # def func(**kwargs):
# #     return kwargs


# # print(func(a=1, b=2, c=3))



# # def intro(**kwargs):
# #     for k, v in kwargs.items():
# #         print(k, "is", v)
# #     print()

# # intro(name="Irina", surname="Sharma", age=22)
# # intro(name="Irina", surname="Sharma", age=22, email="daada@gmail.com", phone = 192851721)


# # def func(a, b, *args, dd=5, cc=7, **kwargs):
# #     return a, b, args, kwargs, dd, cc


# # print(func(1, 2, 3, 4, 5, aa=1, bb=2, cc=3))



# # def db(**kwargs):
# #     my_dict.update(**kwargs)



# # my_dict = {"one": 'first'}
# # db(k1=22, k2=31, k4=91)
# # db(name="Bob", age=31, weight=61, eyes_color='grey')



# # name = "Tom" # global


# # def hi():
# #     global name
# #     global surname
# #     name = "Samuel"
# #     surname = "Rodrigez" # local 
# #     print(f"Hello, {name} {surname}")


# # def bye():
# #     print(f"Good bye, {name}")


# # hi()
# # bye()



# # i = 5


# # def func(arg=i):
# #     print(arg)


# # i = 6
# # func()



# def func(a):
#     x = 2

#     def inner():
#         print("x:", x)
#         return a + x
#     return inner()


# print(func(3))



