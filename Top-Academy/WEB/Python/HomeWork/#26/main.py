from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, a, color):
        self.a = a
        self.color = color

    @abstractmethod
    def per(self):
        pass

    @abstractmethod
    def sq(self):
        pass

    @abstractmethod
    def info(self):
        pass

    def pattern(self):
        for i in range(self.a):
            for j in range(self.a):
                print("* ", end="")
            print()


class Square(Shape):
    def per(self):
        return 4 * self.a

    def sq(self):
        return self.a ** 2

    def info(self):
        print(f"==Квадрат==\nСторона: {self.a}\nЦвет: {self.color}\nПлощадь: {self.sq()}\nПериметр: {self.per()}")
        self.pattern()


class Rectangle(Shape):
    def __init__(self, a, b, color):
        super().__init__(a, color)
        self.b = b

    def per(self):
        return (2 * self.a) + (2 * self.b)

    def sq(self):
        return self.a * self.b

    def info(self):
        print(f"==Прямоугольник==\nДлина: {self.a}\nШирина: {self.b}\nЦвет: {self.color}\nПлощадь: {self.sq()}\n"
              f"Периметр: {self.per()}")
        self.pattern()

    def pattern(self):
        for i in range(self.a):
            for j in range(self.b):
                print("* ", end="")
            print()


class Triangle(Shape):
    def __init__(self, a, b, c, color):
        super().__init__(a, color)
        self.b = b
        self.c = c

    def per(self):
        return self.a + self.b + self.c

    def sq(self):
        p = self.per() / 2
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2), 2)

    def info(self):
        print(f"==Треугольник==\nСторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}\nЦвет: {self.color}\n"
              f"Площадь: {self.sq()}\nПериметр: {self.per()}")
        self.pattern()

    def pattern(self):
        a = self.b - 1
        for i in range(self.a):
            for j in range(a):
                print(end=" ")
            a = a - 1
            for j in range(i + 1):
                print("* ", end="")
            print("\r")


sq = Square(3, "red")
sq.info()
rec = Rectangle(3, 7, "green")
rec.info()
trn = Triangle(11, 6, 6, "yellow")
trn.info()
