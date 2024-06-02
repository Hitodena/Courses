# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"    

#     return wrap


# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"

#     return wrap



# @italic
# @bold
# def hello():
#     return "text"


# print(hello())


# def callback(fn):
#     count = 1
#     def clbk():
#         nonlocal count
#         fn()
#         print(f"Вызов функции: {count}")
#         count += 1    
    
#     return clbk
    

# @callback
# def hello():
#     print("Hello")


# hello()
# hello()
# hello()


# def args_dec(fn):
#     def wrap(arg1, arg2):
#         print(f"Данные: {arg1} {arg2}")
#         # fn(arg1, arg2)
#     return wrap


# @args_dec
# def print_full_name(first, last):
#     print(f"Меня зовут {first} {last}")


# print_full_name("Ирина", "Жердева")



# def args_decor(fn):
#     def wrap(*args, **kwargs):
#         print(f"args: {args}")
#         print(f"kwargs: {kwargs}")
#         fn(*args, **kwargs)

#     return wrap


# @args_decor
# def func(a, b, c, study="Python"):
#     print(f"{a}, {b}, {c} изучают {study}", end="\n\n")

# @args_decor
# def func1(study):
#     print(f'Мне нравится учить {study}')

# func("Борис", "Елизавета", "Светлана", study="JS")
# func("Владимир", "Екатерина", "Виктор")
# func1(study="CSS")

# def decor_args(*arg):
#     def decor(fn):
#         def wrap(x ,y):
#             print(f"{arg[0]}: {x} {arg[1]} {y} = ", end="")
#             fn(x, y)

#         return wrap
#     return decor


# @decor_args('Сумма', '+')
# def summa(a, b):
#     print(a + b)


# @decor_args("Разность", '-')
# def sub(a, b):
#     print(a - b)


# summa(5, 2)
# sub(5, 2)


# def decor_args(arg):
#     def decor(fn):
#         def wrap(x):
#             return arg * fn(x)        
        
#         return wrap
    
#     return decor


# @decor_args(3)
# def return_num(num):
#     return num


# print(return_num(5))
        




# print(int("19"))


# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))



# print(bin(18)) # двоичная
# print(oct(18)) # восьмиричная
# print(hex(18)) # десятичная

# print(0x12)
# print(0o22)
# print(0b10010 + 0x12)




# q = 'pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e*2)
# print("y" in e)

# s = 'python'
# print(s)
# s = s[:3] + 't' + s[4:]
# print(s)


# def changeCharToStr(s, old, new):
#     s2 = ''
#     i = 0

#     while i < len(s):
#         if s[i] == old:
#             s2 = s2 + new
#         else:
#             s2 = s2 + s[i]
#         i += 1

#     return s2


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(str1, "N", "P")
# print(f"str1 = {str1}")
# print(f"str2 = {str2}")


# print("Привет")
# print(u"Привент")



# print("C:\\folder\\file.txt")
# print(r"C:\folder\files\\"[:-1])
# print(r"C:\folder\files" + "\\")


x = 10
y = 5
print(f'{x = }, {y = }')
