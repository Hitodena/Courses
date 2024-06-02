# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j ,end="\n")
#         j += 1
#     print()
#     i += 1



# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+" ,end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1



# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1


# j = 0
# while j < 5:
#     print("-" * j, "*", sep="")
#     j += 1



# for i in "Hello":
#     print(i, end=" ")


# for element in "red", "green", "blue":
#     print(element, end="  ")

# print(range(5)) # start, end, step 


# for i in range(9):
#     print(i, end=" ")

# print()

# for i in range(9, 0, -1):
#     print(i, end=" ")


# n = 9
# for i in range(1, n + 2):
#     print(i, end=" ")



# number = int(input("Введите число: "))
# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i, end=" ")

    
# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")


# for i in range(3):
#     if i == 1:
#         continue
#     print(i)
# else:  
#     print("done") 


# width = int(input("Введите значение (ширина): "))
# height = int(input("Введите значение (высота): "))
# for i in range(height):
#     for j in range(width):
#         if i == 0 or i == height - 1 or j == 0 or j == width - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



# print([i * 5 for i in "Hello"])
# print([i for i in range(30) if i % 2 == 0])



# array = [1, 2, 3, 4, 5, "aboba", 5.1, True]
# print(array[2])
# array[2] = 100
# print(array[2])
# array[2] += 50
# print(array[2])
# array[8] = 1 # not working

# print(len(array))
# indexlastvalue = len(array) - 1
# indexlastvalue = array[-1]


# array = list()
# array = []

# array = list(range(2, 21, 2))
# print(array)



# array = list("all my fellas")
# print(array)
# print(array * 2)
# print(array + [1, 2, 3])




# nums = list(range(2, 100, 10))
# print(nums)

# for i in nums:
#     print(i, end=" ")

# print()

# for i in range(len(nums)):
#     print(i, end=" ")



# a = [0 for i in range(5)]
# print(a)
# b = [i**2 for i in range(1, 6)]
# print(b)
# c = [c * 3 for c in "list"]
# print(c)



# a = [0] * int(input("Введите кол-во значений: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")  # type: ignore
# print(a)


# a = [input("-> ") for i in range(int(input("-> ")))]
# print(a)


sum = 0
array = [float(input("Значение -> ")) for i in range(int(input("Количество символов -> ")))]
for i in range(len(array)):
    sum += array[i]
    mid = sum / len(array)
# highest = max(array)
# lowest = min(array)
highest = array[0]
lowest = array[0]
for i in range(len(array)):
    if array[i] > highest:
        highest = array[i]   
    if array[i] < lowest:
        lowest = array[i]
print(f"Среднее арифметическое: {mid}")
print(f"{highest}")
print(f"{lowest}")


    