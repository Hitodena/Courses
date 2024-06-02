names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item) 
#         else:
#             count += 1
#     return count


# print(count_items(names))



# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])


#print(remove("  Hello\nWorld "))


# Работа с файлами



# f = open(r"D:\Programming\WEB\Python\Lessons\#19\text.txt", "r")
# print(f)
# print(*f)
# print(f.closed)
# f.close()
# print(f.closed)


# f = open(r"WEB\Python\Lessons\#19\text.txt", "r")
# print(f.read(4))
# print(f.read())
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text2.txt", "r")
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text2.txt", "r")
# print(f.readlines(26))
# print(f.readlines())
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text2.txt", "r")
# for line in f:
#     print(line, end="")
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text2.txt", "r")
# print(len(f.readlines()))
# f.close()
# f = open(r"WEB\Python\Lessons\#19\text2.txt", "r")
# count = 0
# for line in f:
#     count += 1
# f.close()
# print(count)


# f = open(r"WEB\Python\Lessons\#19\xyz.txt", "w")
# f.write("New Text.\n")
# f.close()


# f = open(r"WEB\Python\Lessons\#19\xyz.txt", "a")
# lines = ['This is line 1', '\nThis is line 2']
# f.writelines(lines)
# f.close()


# f = open(r"WEB\Python\Lessons\#19\xyz.txt", "w")
# lst = [i for i in range(1, 21)]
# print(lst)
# for index in lst:
#     f.write(str(index) + "\t")
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text3.txt", "w", encoding='utf8')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text3.txt", "r", encoding='utf8')
# rf = f.readlines()
# print(rf)
# rf[1] = "Hello World!\n"

# print(rf)
# f.close()

# f = open(r"WEB\Python\Lessons\#19\text3.txt", "w", encoding="utf8")
# f.writelines(rf)
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text3.txt", "r", encoding='utf8')
# rf = f.readlines()
# pos = int(input())
# del(rf[pos])
# f = open(r"WEB\Python\Lessons\#19\text3.txt", "w", encoding='utf8')
# f.writelines(rf)
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text.txt", "r")
# print(f.read(3))
# print(f.tell()) # текущая позиция курсора
# print(f.seek(1)) # перемещает курсор в позицию
# print(f.read())
# print(f.tell())
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


# f = open(r"WEB\Python\Lessons\#19\text4.txt", "a+")
# print(f.write("I am learning Python\n"))
# print(f.read())
# f.close()


# with open(r"WEB\Python\Lessons\#19\text4.txt", "w+") as f:
#     print(f.write('89678\n12312'))
# print(f.closed)


with open(r"WEB\Python\Lessons\#19\text4.txt", "r") as f:
    for line in f:
        print(line[:3])