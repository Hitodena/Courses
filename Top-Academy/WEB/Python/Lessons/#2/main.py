# num = 4321
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = a*1000 + b*100 + c * 10 + d
# print(num) 


# num = 9753
# res = num % 10 * 1000
# num = num // 10
# res += num % 10 * 100
# num = num // 10
# res += num % 10 * 10
# num = num // 10
# res += num % 10 
# print(res)


# print(int(3.9))


# name = "Виктор"
# age = 38
# print("Меня зовут", name, ". Мне", age, "лет", sep="", end=". ")
# print("hai")


# power = int(input("Введите степень: "))
# number = int(input("Введите число: "))
# a = number ** power
# print(a)


# num = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# num3 = int(input("Введите число: "))
# num4 = int(input("Введите число: "))

# sum = num + num2
# sum2 = num3 + num4
# div = round((sum / sum2), 2)
# print(div)



# b1 = True
# b2 = False
# print(b1 + 1)
# print(b2 + 1)
# if(b2 == 0):
#     print("ничего себе")

# print(bool("")) # False
# print(bool("даже если есть пробел")) # True

# print("Привет" > "Hellah") # 175 > 143


# print(6 > 5 > 3) # True : True => True
# print(4 > 5 < 6) # True : False => False




# 1 + 2 and 2 + 1  # True
# 1 + 2 or 5 + 1 # True
# (not 9-5) # False (True => False) not инвентирует


# a = int(input("Введите 1-сторону: "))
# b = int(input("Введите 2-сторону: "))
# c = int(input("Введите 3-сторону: "))
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or c == b:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")



crows = int(input("Введите кол-во ворон: "))
if crows == 1:
    print(f"На ветке {crows} ворона")
elif crows >= 2 and crows < 5:
    print(f"На ветке {crows} вороны")
elif crows >= 5 and crows == 0:
    print(f"На ветке {crows} ворон")
