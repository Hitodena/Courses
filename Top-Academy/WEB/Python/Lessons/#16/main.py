# s = """
# Несколько строк
# """
# print(s)

# s1 = '''
# Несколько строк
# '''
# print(s1)


"""
Comment
"""



# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2


# print(square(5))
# print(square.__doc__)
# print(len.__doc__)



# from math import pi

# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.


#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания

#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)


# print(cylinder(2, 4))
# print(cylinder.__doc__)
# print(max.__doc__)
# print(len.__doc__)




# print(ord("a"))



# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break



# s = 'Test string for me'
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)

# arr = [(round(sum(arr) / len(arr)))] + arr
# print("Среднее арифметическое:", arr)

# arr += [x for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)

# print(arr.count(arr[-1]) - 3)
# arr.sort(reverse=True)
# print(arr)



# a = 97
# b = 122

# if a < b:
#     a, b = b, a

# for i in range(b, a + 1):
#     print(chr(i), end=" ")



# print("apple" == "Apple")
# print("apple" > "Apple") # 97 > 62


# from random import randint

# shortest = 7
# longest = 10
# min_ascii = 33
# max_ascii = 126

# def random_pass():
#     res = ''
#     for i in range(randint(shortest, longest)):
#         rand_char = chr(randint(min_ascii, max_ascii))
#         res += rand_char
#     return res


# print(f'Ваш случайный пароль: {random_pass()}')



s = "hello, WORLD! I am learning Python"
# print(s.capitalize())
# print(s.upper())
# print(s.upper())
# print(s.swapcase())
# print(s.title())



# print(s.count("l"))
# print(s.count("l", 3))
# print(s.count("l", 3, 10))



# print(s.find("Python1"))
# print(s.find("l", 4, 20))
# print(s.rfind("l"))
# print(s.index("l"))
# print(s.rindex("l"))



# st = input("Введите два слова через пробел: ")
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(second + " " + first)



# "hello, WORLD! I am learning Python"
# print(s.startswith("I am", 14))
# print(s.index("I am"))
# print(s.endswith("on."))


# print('123'.isdigit())
# print("dasdspaвфыхвфыъъхвфы[]".isalpha())

# print("Agc123".isalnum())
# print("AdasdvadsS".islower())
# print("AdasdvadsS".isupper())

# n = input("Введите число: ")
# if n.isdigit():
#     n = int(n)
#     print(n * 2)



# print('py'.center(10))
# print('py'.center(11, "-"))



# print('     py     '.lstrip())
# print('     py     '.rstrip())
# print('     py     '.strip())



# print('https://www.python.org'.strip("/:pths"))



# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python"))
# print(str1.replace("N", "P"))



# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))

# print("..".join(["1", "99"]))

# print(":".join("Hello"))


print("Строка разделенная пробелами".split())
print("www.python.org.ru".split(" ", 2))
print("www.python.org.ru".rsplit(".", 2))

