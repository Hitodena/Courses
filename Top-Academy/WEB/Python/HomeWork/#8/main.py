    
import math as m


def sq(a = 0, b = 0):
    res = int(input("Выбор фигуры:\n 1 - Треугольник(прямоугольный)\n 2 - Прямоугольник\n 3 - Круг\n -->  "))
    if res == 1:
        a = int(input("Введите катет: "))
        b = int(input("Введите катет: "))
        square = (a * b) / 2
        print (square)
    elif res == 2:
        a = int(input("Введите сторону: "))
        b = int(input("Введите сторону: "))
        square = (a * b)
        print (square)
    elif res == 3:
        a = int(input("Введите радиус: "))
        square = (2 * m.pi) * a
        print (square)
    else: 
        print("Данной фигуры нету в списке!")


sq()
