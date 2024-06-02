from abc import ABC, abstractmethod
from math import pi

# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")

#     @abstractmethod
#     def move(self):
#         pass


# class Queen(Chess):
#     def move(self):
#         print("Ферзь перемещен на e2e4")
    

# q = Queen()
# q.draw()



# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius

    
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")


# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length # type: ignore


# class RoundTable(Table):
#     def calc_area(self):
#         return pi * self._radius ** 2 
    

# t1 = SqTable(20, 10)
# print(t1.__dict__)
# print(t1.calc_area())

# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())

# t3 = SqTable(10)
# print(t3.__dict__)
# print(t3.calc_area())





# class Currency(ABC):
#     suffix = "RUB"
    
#     def __init__(self, value):
#         self.value = value
        
#     @abstractmethod
#     def convert_rub(self):
#         pass
    
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
        
#     def show(self):
#         print(f"= {self.convert_rub():.2f} {Currency.suffix}")
        

# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
    
#     def convert_rub(self):
#         return self.value * Dollar.rate_to_rub
    
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
        

# class Euro(Currency):
#     rate_to_rub = 84.12
#     suffix = "EUR"
    
#     def convert_rub(self):
#         return self.value * Euro.rate_to_rub
    
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
    
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for el in d:
#     el.print_value()
#     el.show()

# print("*" * 50)
# for el in e:
#     el.print_value()
#     el.show()





# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
    
#     @abstractmethod
#     def display2(self):
#         pass
    

# class Child(Father):
#     def display1(self):
#         print("Child Class")


# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")


# ch = GrandChild()
# ch.display1()
# ch.display2()
    
    

# Вложенные классы 



# class MyOuter:
#     age = 18
    
#     def __init__(self, name):
#         self.name = name
    
#     def outer_method():
#         print("outer_method")
        
#     def instanse_method(self):
#         print("instance_method")
    
#     class MyInner:
#         def __init__(self, inner_name):
#             self.inner_name = inner_name
            
#         def inner_method(self):
#             print("Вложенный метод", MyOuter.age)
#             MyOuter.outer_method()
#             # MyOuter.instanse_method()


# out = MyOuter("внешний")
# print(out.name)
# inner = out.MyInner("внутренний")
# print(inner.inner_name)
# inner.inner_method()



# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#         self.dk = self.DarkGreen()
        
#     def show(self):
#         print("Name:", self.name)
    
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
        
#         def display(self):
#             print("Name:", self.name)        
    
#     class DarkGreen:
#         def __init__(self):
#             self.name = "Dark Green"
        
#         def display(self):
#             print("Name:", self.name)        
    

# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# d = outer.dk
# d.display()





class Computer:
    def __init__(self):
        self.name = "PC01"
        self.os = self.OS()
        self.cpu = self.CPU()
        
    class OS:
        def system(self):
            return "Windows 10"

    class CPU:
        def brand(self):
            return "Intel"
    
        def model(self):
            return "Core-i7"
        
        
comp = Computer()
my_os = comp.os
my_cpu = Computer().CPU()
print(comp.name, my_os.system(), my_cpu.brand(), my_cpu.model())