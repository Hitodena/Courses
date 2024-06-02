# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last_name': 'Семенов', 'rating': 6},
# ]

# res1 = sorted(players, key=lambda item: item['last_name'])
# print(res1)
# res2 = sorted(players, key=lambda item: item['rating'])
# print(res2)
# res3 = sorted(players, reverse=True ,key=lambda item: item['last_name'])
# print(res3)



# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]
# b = a[0](5,3)
# print(b)

# a = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда")
# }

# a[3]()


# print((lambda a, b, c: a if (a > b) and (b < c) else b if (b < c) else c)(2, 6 ,5))



#map(func, iterable) filter(func, iterable)


# def mult(t):
#     return t ** 2


lst = [2, 8, 12, -5, -18]
# lt = list(map(mult, lst))
# print(lt)

# lt1 = list(map(lambda t: t ** 2, lst))
# print(lt1)

# print(list(map(lambda t: t ** 2, lst)))



# lst = ['1', '2', '3', '4', '5']
# print(lst)
# print(list(map(int, lst)))



# st = [10]
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: x + y, st, num)))



# t = ('abcd', 'abc', 'cdefq', 'def', 'gth')

# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# t2 = tuple(filter(lambda s: s, t))
# print(t2)


# from random import randint
# arr = [randint(0, 40) for i in range(10)]
# print(arr)
# print(list(filter(lambda a: (a >= 10) and (a <= 20), arr)))


# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
# print([x ** 2 for x in range(1, 10) if x % 2])


# Декораторы


# def hello():
#     return 'Hello, I am func "hello"'


# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())


# super_func(hello)



# def hello():
#     return 'Hello, I am func "hello"'


# test = hello
# print(id(test()))
# print(id(hello()))
# print(test())



def my_decorator(func): #декорирующая функция
    def inner():
        print("*" * 50)
        func()
        print("-" * 50)
    return inner


@my_decorator #декоратор
def func_test(): # декорируемая функция
    print("Hello, I am func 'func_test'")

func_test()


@my_decorator
def hello():
    print("hello")
hello()
    