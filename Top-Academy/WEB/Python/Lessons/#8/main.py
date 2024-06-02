# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two


# m = maximum(9, 16)
# print(m)


# def ab(a, b):
#     if a > b:
#         return(a - b)
#     else:
#         return(a+b)

# print(ab(int(input()), int(input())))


# def cube(a):
#     return a ** 3


# for i in range(1, 11):
#     print(i, "в кубе=",cube(i))



# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst


# print(change([5,1,2,3,4,5,6,7,8]))
# print(change(["c", "a", "q"]))



# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False


# print(func(10, 5))
# print(func(5, 10))
# a = 5
# b = 10
# if func(a, b):
#     print("Первое больше второго")
# else:
#     print("Второе число больше второго")




# def checkpass(password):
#     has_upper = False
#     has_lower = False
#     has_num = False

#     for symb in password:
#         if "A" <= symb <= "Z":
#             has_upper = True
#         if "a" <= symb <= "z":
#             has_lower = True
#         if "0" <= symb <= "9":
#             has_num = True

#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False


# p = input("Введите пароль: ")
# if checkpass(p):
#     print("Надежный пароль")
# else:
#     print("Ненадёжный пароль")




# def get_sum(a = 0, b = 0, c = 0, d = 1):
#     return a + b + c + d


# print(get_sum(1, 5, 7, 9))
# print(get_sum(1, 5, 7))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d = 2))



# def set_param(c=20, s="-"):
#     print(s * c) # "-" * 20


# set_param()
# set_param(7)
# set_param(20, s="#")



# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         print(n)
#         n //= 10
#     return s


# print("Сумма чётных цифр:")
# print(digit_sum(9874823))
# print(digit_sum(38271))
# print(digit_sum(123456789))

# print("Сумма нечётных цифр:")
# print(digit_sum(9874823, even=False))


# def display_info(name,age, nm):
#     print("Name:", name, "\nAge:", age)

# display_info(nm="Igor", age=23, name="Ira")


# a = "hello"
# b = "hello"
# print(a == b)
# print(a is b) # True на одну ячейку памяти

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 == lst2)
# print(lst1 is lst2) # False


# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())



a = "red", "blue", "green"
print(a)