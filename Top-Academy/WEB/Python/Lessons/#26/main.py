# class Cat:
#     def __init__(self, name):
#         self.name = name
        
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"

#     def __str__(self):
#         return f"{self.name}"
    

# cat = [Cat("Пушок")]
# print(cat)]


# class Point:
#     def __init__(self, *args):
#         self.coord = args  # tuple(1, 2)
#         self.color = "red"
#         self.width = 2
#
#     def __len__(self):
#         return len(self.coord)
#
#
# p = Point(1, 2, 5)
# print(len(p))
#
# s = list((1, 2))
# print(len(s))

# import math


# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(10, 20)
# print(p1.x, p1.y)
# # p1.z = 30
# # print(p1.z)
# p1.length = 20
# print(p1.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2(1, 2)
# print("pt1 =", pt1.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# class Point3D(Point):
#     __slots__ = ('x', 'y', 'z')
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = 3
#
#
# pt1 = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# pt3.z = 3  # slots в дочерние не наследуется
# print(pt3)
# print(pt3.__dict__)


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("WorldDestroyer")
# beast.bark()
# beast.sleep()
# beast.play()


# class A:
#     def __init__(self):
#         print("Инициализатор класса A")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса A")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#         B.__init__(self)
#         C.__init__(self)
#
#
# d = D()
# print(D.mro())
# print(D.__mro


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         # Styles.__init__(self, color, width)
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp} {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()


# mixin

# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init Mixin")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class Laptop(Goods, MixinLog):
#     pass
#
#
# n = Laptop("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
#
# n2 = Laptop("ASUS", 2, 43650)
# n2.print_info()
# n2.save_sell_log()


# Перегрузка операторов

# 24 * 60 * 60 = 86400 - число секунд в одном дне

class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return x if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec == other.sec:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


c1 = Clock(100)
c2 = Clock(200)
# c3 = Clock(300)
# c4 = c1 + c2 + c3
print(c1.get_format_time())
print(c2.get_format_time())
# print(c3.get_format_time())
# print(c4.get_format_time())
# c1 += c2
print(c1.get_format_time())
# if c1 == c2:
#     print("Время равное")
# else:
#     print("Время разное")
if c1 != c2:
    print("Время разное")
else:
    print("Время одинаковое")
