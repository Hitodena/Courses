PATH = r"WEB\Python\Lessons\#20"
# file_name = PATH + r"\res.txt"
# lst = [4.5, 2.8, 3.9, 1.8, 0.3, 4.33, 7.777]

# def get_line(lt):
#     lt = map(str, lt)
#     return ' '.join(lt)

# with open(file_name, "w") as f:
#     # f.write(str(lst))
#     f.write(get_line(lst))

# with open(file_name, "r") as f:
#     st = f.read()

# print(st)
# print(type(st))

# nums = list(map(float, st.split()))
# print(nums)
# print(type(nums[0]))


# a = 5

# if a == 5:
#     b = 10

# print(b)

# for i in range(12):
#     b = 10
# print(b)


# def func():
#     b = 10


# func()
# print(b)


# def longest_words(file):
#     with open(file, "r", encoding="utf-8") as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         res = [i for i in w if len(i) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res


# print(longest_words(PATH + r'\test.txt'))



# text = "Строка №1\nСтрока №2\nСтрока №3"

# with open(PATH + r'\one.txt', "w", encoding="utf-8") as f:
#     f.write(text)


# with open(PATH + r'\one.txt', 'r', encoding="utf-8") as fr, open(PATH + r'\two.txt', "w", encoding="utf-8") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)





# OS OS.PATH


import os

# print(os.getcwd()) # текущая директория
# print(os.listdir()) # текущая папка
# print(os.listdir(".."))


# os.mkdir(r"WEB\Python\Lessons\#20\f")
# os.rmdir(r"WEB\Python\Lessons\#20\f") # удаление пустой папки


# os.remove(r"WEB\Python\Lessons\#20\one.txt")
# os.rename(r"WEB\Python\Lessons\#20\res.txt", r"WEB\Python\Lessons\#20\f")

# os.renames #переименование файла и папки, перемещает документы, создавая промежуточные директории


# for root, dirs, files in os.walk(r"WEB\HTML", topdown=False):
#     print(f"Root: {root}")
#     print(f"\tSubdirs: {dirs}" )
#     print(f"\t\tFiles: {files}")



# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветке {root_tree}')
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print('-' * 50)


# import os.path
# print(os.path.split(r"D:\Programming\WEB\Python\#20\two.txt"))
# print(os.path.join(r'D:\Programming\WEB\Python','HomeWork', '#20', ))






