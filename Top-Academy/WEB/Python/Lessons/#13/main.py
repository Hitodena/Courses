# def func1():
#     a = 6

#     def func2(b):
#         a = 4
#         print(a + b)
    
#     print("a:", a)
#     func2(4)


# func1()

# def fn1():
#     x = 25

#     def fn2():
#         x = 33
    
#         def fn3():
#             nonlocal x
#             x = 55
             
#         fn3()
#         print("fn2.x =", x)
    
#     fn2()
#     print("fn1.x =", x)


# fn1()


# def outer(a1, b1, a2, b2):    
#     a = 0 
#     b = 0


#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print("a:", a)
#         print("b:", b)

#     inner()
#     return [a, b]


# замыкание

# def outer(n):
#     def inner(x):
#         return n + x
    
#     return inner


# out1 = outer(5)
# print(out1(10))
# out2 = outer(6)
# print(out2(12))
# print(outer(5)(10))



# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]

#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
    
#     return func2


# func = func1()
# print(func())



# def func(city):
#     count = 0

#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)

#     return inner


# res1 = func("Moscow")
# res1()
# res1()
# res2 = func("Minsk")
# res2()
# res2()
# res3 = func("Soul")
# res3()
# res3()
# res3()
# res3()


# def func(x, y):
#     return x + y


# print((lambda x, y: x + y)(2, 5))


# print(lambda *args: sum(args))



# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )

# for t in c:
#     print(t("abc_"))



# def outer(n):
#     def inner(x):
#         return n + x
    
#     return inner


# f = outer(5)
# print(f(10))

# def outer1(n):
#     return lambda x: n + x

# print((lambda n: lambda x: n + x)(5)(10))




# print((lambda x: lambda y: lambda z: x + y + z))

def func(i):
    return i[1]


d = {"b": 15, "a": 7, "c": 3}
print(d)
lst = list(d.items())
print(lst)
lst.sort(key=func)
# lst.sort(key=lambda i: i[1])
print(lst)
print(dict(lst))