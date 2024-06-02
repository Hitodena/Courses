# number = int(input("Введите число: "))

# if number % 2 == 0:
#     print(f"Число {number} - чётное")
# else:
#     print(f"Число {number} - нечётное")

number = int(input("Введите количество копеек(1 - 99): "))
if number > 99 or number < 1:
    print("Неверное число")
else:
    if (number == 11 or number == 12 or number == 13 or number == 14):
        print(f"{number} копеек")
    else:
        if (number % 10 == 2 or number % 10 == 3 or number % 10 == 4):
            print(f"{number} копейки")
        elif (number % 10 == 1):
            print(f"{number} копейка")
        elif (number % 10 == 5 or number % 10 == 6 or number % 10 == 7 or number % 10 == 8 or number % 10 == 9):
            print(f"{number} копеек")
