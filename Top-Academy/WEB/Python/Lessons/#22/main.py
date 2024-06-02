import math

# class Robot:
#     k = 0
    
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация робота: {self.name}")
#         Robot.k += 1
        
#     def __del__(self):
#         print(self.name, "выключился")
#         Robot.k -= 1
        
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
    
    
#     def say_hi(self):
#         print(f"Меня зовут: {self.name}")
        

# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print(f"Количество роботов: {Robot.k}")
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print(f"Количество роботов: {Robot.k}")
# droid3 = Robot("P-2CO")
# print(f"Количество роботов: {Robot.k}")
# print("\nЗдесь роботы могут работать\n")
# print("Роботы закончили свою работу")
# del droid1
# del droid2
# del droid3
# print(f"Количество роботов: {Robot.k}")




# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
            
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
    
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должна быть числом")
            
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата Y должна быть числом")
    
#     def get_x(self):
#         return self.__x
    
#     def get_y(self):
#         return self.__y
    

# p1 = Point(5, 10)
# p1.set_x(50)
# print(p1.get_x())
# p1.set_y(100)
# print(p1.get_y())
# p1._Point.__x = 111
# print(p1.__dict__)
# print(p1._Point.__x)


# public self.a
# protected self._a
# private self.__a



# class Rectangle:
#     __slots__ = ["__length", "__width"]
    
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
        
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
    
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
    
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width

#     def get_length(self):
#         return self.__length
    
#     def get_width(self):
#         return self.__width
    
#     def get_sq(self):
#         return self.__length * self.__width
    
#     def get_pr(self):
#         return 2*(self.__length + self.__width)
    
#     def get_hyp(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
    
#     def get_print(self, symbol):
#         print((symbol * self.__width + "\n") * self.__length)
    
# rect = Rectangle(4, 12)
# rect.set_length(3)
# rect.set_width(9)
# print(rect.get_length(), rect.get_width())
# print(rect.get_sq())
# print(rect.get_pr())
# print(rect.get_hyp())
# rect.get_print("*")




# class Point:
    
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
        
#     def __set_x(self, x):
#         self.__x = x
#         print("Сеттер")
        
#     def __get_x(self):
#         print("Геттер")
#         return self.__x
    
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
        
#     x = property(__get_x, __set_x, __del_x)


# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)



# class Point:
    
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
     
#     @property   
#     def x(self):
#         print("Геттер")
#         return self.__x  
    
#     @x.setter
#     def x(self, x):
#         if Point.checher....
#         self.__x = x
#         print("Сеттер")
    
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
        



# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)



# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
        
#     @property
#     def kg(self):
#         return self.__kg
    
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы только числами")
            
#     def to_pound(self):
#         return self.__kg * 2.205


# weight = KgToPounds(12)
# print(weight.kg, "кг =>", weight.to_pound(), "фунтов")




class Point:
    __count = 0
    
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1
        
    @staticmethod
    def get_count():
        return Point.__count
    

p1 = Point()
p2 = Point()
p3 = Point()

print(Point.get_count())