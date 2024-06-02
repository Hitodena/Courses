quantity = int(input("Введите количество символов: ")) 
symbol = input("Введите символ: ")
orient = int(input("Введите ориентацию символов(0 - вертикальная, 1 - горизонтальная): "))
def out(a, b, c):
    a = a
    b = b
    c = c
    if c == 0:
        for i in range(a):
            print(b)
    else:
        print(f"{b * a}")
out(quantity, symbol, orient)