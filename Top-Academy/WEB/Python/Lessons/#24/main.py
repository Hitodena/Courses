import re




# class UserData:
#     def __init__(self, fio, age, ps, weight):        
#         self.fio = fio
#         self.age = age
#         self.ps = ps
#         self.weight = weight
    
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формать ФИО")
#         letters = "".join(re.findall('[a-zа-яё-]', fio, re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис.")

#     @staticmethod
#     def verify_age(age):
#         if not isinstance(age, int) or age < 14 or age > 120:
#             raise TypeError("Возраст должен быть числом в диапозоне от 14 до 120 лет.")

#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 30:
#             raise TypeError("Вес должен быть вещественным числом")

#     @staticmethod
#     def verify_ps(value):
#         if not isinstance(value, str):
#             raise TypeError("Паспорт должен быть строкой.")
#         s = value.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть цифрами")
            
#             @property
#             def fio(self):
#                 return self.fio
            
#             @fio.setter
#             def fio(self, value):
#                 self.verify_fio(value)
#                 self.fio = value
            
#             @property
#             def age(self):
#                 return self.age
            
#             @age.setter
#             def age(self, value):
#                 self.verify_age(value)
#                 self.age = value
                
#             @property
#             def ps(self):
#                 return self.ps
            
#             @ps.setter
#             def ps(self, value):
#                 self.verify_ps(value)
#                 self.ps = value
            
#             @property
#             def weight(self):
#                 return self.weight
            
#             @weight.setter
#             def weight(self, value):
#                 self.verify(value)
#                 self.weight = value


# user = UserData("Волков Игорь Николаевич", 35, "1234 567890", 80.4)




# Наследование 








# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
    
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"


# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Переопределнный инициализатор Prop")
    
#     def get_width(self):
#         return self.__width


# class Line(Prop):
#     def __init__(self, *args):
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         print("Переопределенный инициализатор Line")
    
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")


# class Rect(Prop):        
#         def draw_rect(self):
#             print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")


# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()   
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()     
# # print(issubclass(Point, object))
# # print(issubclass(Rect, Prop))





# class Figure:
#     def __init__(self, color):
#         self.color = color


# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
    
#     @property
#     def width(self):
#         return self.__width
    
#     @width.setter
#     def width(self, width):
#         if width > 0:
#             self.__width = width
#         else:
#             raise ValueError("Ширина должна быть положительным числом.")
        
#     @property
#     def height(self):
#         return self.height
    
#     @height.setter
#     def height(self, height):
#         if height > 0:
#             self.__height = height
#         else:
#             raise ValueError("Высота должна быть положительным числом.")
        
#     def square(self):
#         print(f"Площадь {self.color} прямоугольника: {self.__height * self.__width}")
#         return self.__width * self.__height 
        
        
# rect = Rectangle(20, 10, "green") 
# print(rect.color)
# rect.width = 50
# print(rect.width)
# rect.square()





# class Rect():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
        

# class RectBG(Rect):
#     def __init__(self, width, height, color):
#         super().__init__(width, height)    
#         self.color = color
        
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.color)
        

# class RectBorder(Rect):
#     def __init__(self, width, height, color, px, typeof,):
#         super().__init__(width, height)
#         self.color = color
#         self.px = px
#         self.typeof = typeof
    
#     def show_rect(self):
#         super().show_rect()
#         print(f"Рамка: {self.px} {self.typeof} {self.color}")

    

# shape1 = RectBG(400, 200, "black")
# shape1.show_rect()
# shape2 = RectBorder(400, 300, "red", "1px", "solid")  
# shape2.show_rect()  
        
        
        
        
        
# class Vector(set):
#     def __str__(self):
#         return " ".join(map(str, self))


# v = Vector({1, 2, 3})
# print(v)




# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     def __str__(self):
#         return f"({self.__x}, {self.__y})"


# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width


# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
    
#     def set_coord(self, sp: Point = None, ep: Point = None): #type:ignore
#         if ep is None:    
#             self._sp = sp
#         elif sp is None:
#             self._ep = ep
#         else:
#             self._cp = ep
#             self._sp = sp
        
        
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(12, 18), ep=Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20)) #type:ignore
# line.draw_line()

# line.set_coord(ep=Point(500, 700)) # type: ignore
# line.draw_line()





a = 5
a = 6
print(a)