# # Функторы
#
#
# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1(" :?.Hello World! "))
#
#
# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars

# def __call__(self, *args, **kwargs):
#     if not isinstance(args[0], str):
#         raise ValueError("Аргумент должен быть строкой")
#
#     return args[0].strip(self.__chars)

# def __call__(self, string):
#     if not isinstance(string, str):
#         raise ValueError("Аргумент должен быть строкой")
#
#     return string.strip(self.__chars)


# s2 = StripChars("?:!.; ")
# print(s2(" :?.Hello World! "))


# class decorator


# class MyDec:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         # print("Перед вызовом функции")
#         # self.fn(x, y)
#         # print("После вызова функции")
#         return f"Перед вызовом функции\n{self.fn(x, y)}\nПосле вызова функции"


# @MyDec
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         return f"Результат: {self.fn(x, y) ** 2}"
#
#
# @Power
# def func_test(a, b):
#     return a * b
#
#
# print(func_test(5, 5))


# class MyDec:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         # print("Перед вызовом функции")
#         # self.fn(x, y)
#         # print("После вызова функции")
#         return f"Перед вызовом функции\n{self.fn(*args, **kwargs)}\nПосле вызова функции"
#
#
# @MyDec
# def func(a, b):
#     return a * b
#
# @MyDec
# def func1(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, 5, 7))


# class MyDec:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             return (f"Перед вызовом функции\n{self.arg} {args[0]} x {args[1]} = {fn(*args, **kwargs)}"
#                     f"\nПосле вызова функции")
#         return wrap
#
#
# @MyDec("Произведение:")
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             return f"Результат: {fn(*args, **kwargs) ** self.arg}"
#         return wrap
#
#
# @Power(3)
# def func_test(a, b):
#     return a * b
#
#
# print(func_test(2, 2))

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap


# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Некрасов")
# p1.info()


# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(5))
# print(obj.doubler(5))

# Дескриптор


# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def get(self):
#         return self.__value
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} не является строкой!")
#         self.__value = value


# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value


# p = Person("Иван", "Петров")
# print(p.name.get())
# p.name.set("Игорь")
# print(p.name.get())


# Дескриптор (__get__, __set__, __set_name_, __delete__)


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Иван", "Петров")
# print(p.name)
# print(p.surname)


class NonNegative:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.__name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError()
        # instance.__dict__[self.__name] = value
        setattr(instance, self.name, value)


class Order:
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


apple_order = Order("Apple", 5, 10)
apple_order.price = 15
print(apple_order.total())
print(apple_order.price)
