# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
    
#     @staticmethod
#     def dec(x):
#         return x - 1
    

# print(Change.inc(10), Change.dec(10))



# class Fact:
    
#     @staticmethod
#     def max(*args):
#         return max(args)
    
#     @staticmethod
#     def min(*args):
#         return min(args)
    
#     @staticmethod
#     def fact(arg):
#         factor = 1
#         for i in range(1, arg + 1):
#          # 5! = 1 * 2 * 3 * 4 * 5
#             factor *= i
#         return factor
    
#     @staticmethod
#     def avg(*args):
#         avg = sum(args) / len(args)
#         return avg
    
# print(Fact.max(3, 5, 7, 9))
# print(Fact.min(3, 5, 7, 9))
# print(Fact.fact(5))
# print(Fact.avg(3, 5, 7, 9))



# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
    
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date1 = cls(day, month, year)
#         return date1
    
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12
    
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
    
  
# dates = [
#     "15.12.2024",
#     "23-10-2023",
#     "01.01.2021",
#     "12.31.2020"
# ]

# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         print(date.string_to_db())
#     else:
#         print("Неправильная дата или формат строки") 
  
# string_date = "23.10.2023"
# day, month, year = list(map(int, string_date.split(".")))
# date = Date(day, month, year)
# print(date.string_to_db())




# class Account:
#     rate_USD = 0.013
#     rate_EUR = 0.011
#     sfxr = "RUB"
#     sfxu = "USD"
#     sfxe = "EUR"
    
#     def __init__(self, owner, num, percent, value):
#         self.owner = owner
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счёт #{self.num}, принадлежащий {self.owner} был открыт.")
#         print("*" * 50)
    
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счёт #{self.num} принадлежащий {self.owner} был закрыт.")
    
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.sfxr}") 
        
#     @staticmethod
#     def convert(value, rate):
#         return value * rate

#     def convert_to_usd(self):
#         usd_value = Account.convert(self.value, Account.rate_USD)
#         print(f"Состояние счёта: {usd_value} {Account.sfxu}")
        
#     def convert_to_eur(self):
#         eur_value = Account.convert(self.value, Account.rate_EUR)
#         print(f"Состояние счёта: {eur_value} {Account.sfxe}")
        
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_USD = rate
    
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_EUR = rate
        
#     def set_owner(self, owner):
#         self.owner = owner
    
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены.")
#         self.print_balance()
        
#     def withdraw_money(self, value):
#         if value > self.value:
#             print("Недостаточно средств!")    
#         else:    
#             self.value -= value
#             print(f"С вашего счёта снято {value} {Account.sfxr}.")
#         self.print_balance()
    
#     def add_money(self, value):
#         self.value += value
#         print(f"{value} {Account.sfxr} были успешно добавлены на вас счёт!")
#         self.print_balance()
        
#     def print_info(self):
#         print("Информация о счёте:")
#         print("-" * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.owner}')
#         self.print_balance()        
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)        
    
    
# acc = Account("Лавашина", 125891, 0.12, 294751)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()

# Account.set_usd_rate(0.011)
# Account.set_eur_rate(0.009)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()

# acc.set_owner("William")
# acc.print_info()
# print()

# acc.add_percents()
# print()

# acc.withdraw_money(11283)
# print()

# acc.add_money(123129)
# print()

# del acc

import re




class UserData:
    def __init__(self, fio, age, ps, weight):
        self.verify_fio(fio)
        self.verify_age(age)
        self.verify_ps(ps)
        self.verify_weight(weight)
    
    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формать ФИО")
        letters = "".join(re.findall('[a-zа-яё-]', fio, re.IGNORECASE))
        for s in f:
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквы и дефис.")

    @staticmethod
    def verify_age(age):
        if not isinstance(age, int) or age < 14 or age > 120:
            raise TypeError("Возраст должен быть числом в диапозоне от 14 до 120 лет.")

    @staticmethod
    def verify_weight(w):
        if not isinstance(w, float) or w < 30:
            raise TypeError("Вес должен быть вещественным числом")

    @staticmethod
    def verify_ps(ps):
        if not isinstance(ps, str):
            raise TypeError("Паспорт должен быть строкой.")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")
        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть цифрами")


user = UserData("Волков Игорь Николаевич", 35, "1234 567890", 80.4)
