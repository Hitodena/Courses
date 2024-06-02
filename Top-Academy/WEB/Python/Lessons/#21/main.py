import os
import time

# print(os.path.exists(r'WEB\Python'))
# # print(os.path.getsize(r'WEB\Python'))
# b = os.path.getsize(r'WEB\Python')
# print(b, "б")
# print(b // 1024, "кб")


# path = r"WEB\Python"
# print(os.path.getctime(path))
# print(os.path.getatime(path))
# print(os.path.getmtime(path))

# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getatime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path))))





# ООП

# Инкапсуляция - сокрытие
# Наследование - родительский класс, дочерний класс
# Полиморфизм - много форм взаимодействия


# 
# class Point:
#     """
#     dadad
#     """
#     # свойства - (поля, переменные)
#     # методы - фунцкции
#     # атрибуты - свойства + методы
#     x = 1
#     y = 1


# p1 = Point() # экземпляр класса Point
# print(p1.x, p1.y, sep="|")
# print(type(p1))
# print(Point.__name__)
# print(Point.__doc__)
# print(dir(Point))



# class Point:
#     x = 1
#     y = 1


# p1 = Point()
# p1.x = 10
# p1.y = 20
# p1.z = 30 #type: ignore
# print(p1.x, p1.y, p1.z) #type: ignore
# print(p1.__dict__)

# p2 = Point()
# p2.x = 100
# print(p2.x, p2.y)
# print(p2.__dict__)

# # print(id(Point))
# # print(id(p1))
# # print(id(p2))



# class Point:
#     x = 1
#     y = 1

#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)


# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# # Point.set_coord(p1)

# p2 = Point()
# # p2.x = 50
# # p2.y = 100
# p2.set_coord(50, 100)
# # Point.set_coord(p2)





# class Person:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
    
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
    
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
        
#     def set_name(self, name):
#         self.name = name
        
#     def set_bithday(self, birthday):
#         self.birthday = birthday
    
#     def get_name(self):
#         return self.name
    
#     def get_birthday(self):
#         return self.birthday
        
        
        

# h1 = Person()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())
# print(h1.get_birthday())
# h1.set_bithday("23.12.1990")
# print(h1.get_birthday())





class Person:
    skill = 30 # статические
    count = 0
    # name = ""
    # surname = ""
    def __init__(self, name, surname): # Инициализатор
        self.name = name # динамические
        self.surname = surname
        print("Инициализатор")
        Person.count += 1
    
    def __del__(self): # финализатор
        print("Удаление экземпляра: ", self.__class__.__name__)
        
        
    def print_info(self):
        print("Данные сотрудника: ", self.name, self.surname)
    
    def add_skill(self, key):
        self.skill += key
        print("Квалификация сотрудника:", self.skill, end="\n\n")


p1 = Person("Виктор", "Резник")
p1.print_info()
p1.add_skill(3)
# del p1
# p1 = 5
print(p1.count)

p2 = Person("Анна", "Долгих")
p2.print_info()
p2.add_skill(2)
print(p2.count)