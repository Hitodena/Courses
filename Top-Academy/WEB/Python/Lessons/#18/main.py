import re

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "Hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# text = "Я ищу совпадение в 2024 году. И я их найду в два счёта."
# reg = "я"

# print(re.findall(reg, text, re.IGNORECASE))
# print(re.findall(reg, text, re.I))



# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text, re.DOTALL))
# print(re.findall(r"one$", text, re.MULTILINE))


# print(re.findall('''
# [A-Za-z0-9._-]+
# @
# [A-Za-z._-]+
# ''', 'test@mail.ru', re.VERBOSE))



# text = """Python
# python,
# PYTHON"""

# reg = "(?mi)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))



# s = "Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg,s))

s = "int = 4 float = 4.0f, double = 8.0"
# # template = r"\w+\s*=\s\d[.\w+]*"
# # template = r"(?:int|float)\s*=\s*\d[.\w+]*"
# template = r"(int|float)\s*=\s*(\d[.\w+]*)"
# print(re.findall(template,s))
# print(re.search(template,s))

# (?: ....) - группирующая скобка не является сохраняющей

# s = "5 + 7 * 2 - 4"
# reg = r"\s*([*+-])\s*"
# print(re.split(reg, s))



# s = "01-12-2024"
# reg = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# print(re.search(reg, s).group()) #type: ignore
# m = re.search(reg, s)
# print(m[0]) #type: ignore
# print(m[1]) #type: ignore
# print(m[2]) #type: ignore
# print(m[3]) #type: ignore
# print(re.search(reg, s).group(0)) #type: ignore
# print(re.search(reg, s).group(1)) #type: ignore
# print(re.search(reg, s).group(2)) #type: ignore
# print(re.search(reg, s).group(3)) #type: ignore


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0


# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"


# print(re.sub(r"\s*(\w+)\s", replace_find, text))


# s = "Самолёт прилетает 10/23/2024. Будем рады видеть вас после 10/24/2024."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))


# s = "yandex.com and yandex.ru"
# reg = r"([a-z0-9-]{2,}\.[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))


# Рекурсия



# def elevator(n): # 0
#     if n == 0:
#         print("Вы в подвале")
#         return ### прерывание функции
#     print("=>", n) # 1 
#     elevator(n - 1) # 5 4 3 2 1 ### этой #### стек 
#     print(n, end=" ") # выводит целый стэк

# # stack -
#   5 -> <-
#       4 -> <-
#           3 -> <-
#               2 -> <-
#                    1 -> <-



# n1 = int(input("На каком вы этаже: " ))
# elevator(n1)



# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res


# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])


# print(sum_list([1, 3, 5, 7, 9]))



def to_str(n, base):
    convert = "0123456789ABCDEF"
    if n < base:
        return convert[n]
    else:
        return to_str(n // base, base) + convert[n % base]
    

print(to_str(254, 16)) # 
    