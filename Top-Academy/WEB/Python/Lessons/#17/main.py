# Регулярные выражения

import re

# print(re.findall(reg, s)) # возвращает список содержащий все совпадения

# print(re.search(reg, s)) # месторасположение первого совпадения с объектом
# # print(re.search(reg, s).span()) # type:ignore
# # print(re.search(reg, s).start()) # type:ignore
# # print(re.search(reg, s).end()) # type:ignore
# # print(re.search(reg, s).group()) # type:ignore

# print(re.match(reg, s)) # поиск совпадения с темплейтом в начале строки

# print(re.split(reg, s, 1)) # возвращает список, в котором строка разбита по шаблону

# print(re.sub(reg, "!", s, 2)) # поиск и замена


# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 98673 Hello"
# reg = "[21][0-9][0-9][0-9]"
# reg = "[А-яЁё]"
# reg = "[A-Za-z]"
# reg = r"\."
# reg = r"[A-Za-z\[\]-]"
# reg = r"[^0-9]" ^ - исключая, всё ^a - всё, кроме a
# reg = r"[^А-яЁёA-Za-z0-9]"
# print(re.findall(reg, s))

# print(ord("а"))
# print(ord("я"))
# print(ord("ё"))


# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T14:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09"
# pattern = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(pattern, st))



# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 98673 Hel_lo"
# reg = r"\D"
# reg = r"\s"
# reg = r"\w"
# reg = r"\AЯ ищу"
# reg = r"lo\Z"
# reg = r"/bсов"
# print(re.findall(reg, s))



# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 98673 Hel_lo 20000000000000000000000"
# # reg = r"\d+"
# # reg = r"[20]*"
# reg = r"[20]*"
# print(re.findall(reg, s))

# Кол-во повторений
# +  -  от 1 до бесконечности
# *  -  от 0 до бесконечности
# ?  -  от 0 до 1



# d = "Цифры: 7, +17, -42, 0013, 0.3"
# # reg = r"[+-]?\d+\.?\d?"
# reg = r"[+-]?[\d.]+"
# print(re.findall(reg, d))



# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"\s#.*", "", s))
# print(re.sub('-', '.', s))
# print("Дата рождения:", re.sub('-' ,'.' , re.sub(r"\s#.*", "", s)))
# print("Дата рождения:", re.sub('-' ,'.' , "05.03.1987"))



# s = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year =1831"
# reg = r"\w+\s*=\s*[^;]+"
# print(re.findall(reg, s))




# s = "12 сентября 2024 года 568789456"
# reg = r"\d{,4}" # количество повторений в фигурных скобках
# print(re.findall(reg, s))



# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\.$" # $ - последний элемент
# print(re.findall(reg, s))






