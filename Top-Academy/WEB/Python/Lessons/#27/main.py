# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[2])  # нужно перегрузить метод, чтобы понять, что возвращается для класса
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return x if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec == other.sec:
#             return True
#         return False
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 60
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.min = s + 60 * value + h * 3600
#         if key == "hour":
#             self.hour =
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 11
# print(c1["hour"], c1["min"], c1["sec"])


# from random import choice, randint


# class Cat:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         if self.sex == "M":
#             return f"{self.name} is a good boy!"
#         if self.sex == "F":
#             return f"{self.name} is a good girl!"
#         else:
#             return f"{self.name} is a good kitty!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, sex={self.sex}"
#
#     def __add__(self, other):
#         return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# print(cat1)
# print(cat2)
# print(cat1 + cat2)


#  Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w * self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())

# from abc import abstractmethod, ABC
#
#
# class Animal(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @abstractmethod
#     def info(self):
#         pass
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Cat(Animal):
#     def info(self):
#         return f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog(Animal):
#     def info(self):
#         return f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} гавкает"
#
#
# cat1 = Cat("Пушок", 2.5)
# dog1 = Dog("Мухтар", 4)
#
# for animal in (cat1, dog1):
#     print(animal.info())
#     print(animal.make_sound())


class Human:
    def __init__(self, ln, fn, age):
        self.ln = ln
        self.fn = fn
        self.age = age

    def info(self):
        print(f"\n{self.ln} {self.fn} {self.age}", end=" ")


class Student(Human):
    def __init__(self, ln, fn, age, spec, group, rating):
        super().__init__(ln, fn, age)
        self.spec = spec
        self.group = group
        self.rating = rating

    def info(self):
        super().info()
        print(f"{self.spec} {self.group} {self.rating}", end=" ")


class Teacher(Human):
    def __init__(self, ln, fn, age, spec, exp):
        super().__init__(ln, fn, age)
        self.spec = spec
        self.exp = exp

    def info(self):
        super().info()
        print(f"{self.spec} {self.exp}", end=" ")


class Graduate(Student):
    def __init__(self, ln, fn, age, spec, group, rating, topic):
        super().__init__(ln, fn, age, spec, group, rating)
        self.topic = topic

    def info(self):
        super().info()
        print(f"{self.topic}", end=" ")


group = [
    Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
    Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
    Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
    Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
    Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
    Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)]

for i in group:
    i.info()
