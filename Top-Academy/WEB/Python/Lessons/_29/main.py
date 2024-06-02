# # MyList = type(
# #     "MyList",
# #     (list,),
# #     dict(get_length=lambda self: len(self))
# # )
# #
# #
# # lst = MyList()
# # lst.append(5)
# # lst.append(7)
# # print(lst, lst.get_length())
#
#
# # Модули
#
#
# # import module.hello
# # import module.summ
# #
# # a = module.hello.hello()
# # b = module.summ.summa(1, 5, 6)
#
# from geometry import rectangle, square, triangle
#
# def run():
#     r1 = rectangle.Rectangle(1, 2)
#     r2 = rectangle.Rectangle(3, 4)
#
#     s1 = square.Square(10)
#     s2 = square.Square(20)
#
#     t1 = triangle.Triangle(1, 2, 3)
#     t2 = triangle.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == "__main__":
#     run()


# from car import electrical
#
#
# if __name__ == "__main__":
#     e_car = electrical.ElectroCar("Tesla", "T", 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()


# class Employee:
#     def __init__(self, code, name):
#         self.code = code
#         self.name = name
#
#
# class SalaryEmployee(Employee):
#     """Административные работники, имеющие фиксированную зарплату"""
#     def __init__(self, code, name, weekly_salary):
#         super().__init__(code, name)
#         self.ws = weekly_salary
#
#     def calculate_payroll(self):
#         return self.ws
#
#
# class HourlyEmployee(Employee):
#     """Сотрудники, имеющие почасовую зарплату"""
#     def __init__(self, code, name, time, rate_per_hour):
#         super().__init__(code, name)
#         self.time = time
#         self.rph = rate_per_hour
#
#     def calculate_payroll(self):
#         return self.time * self.rph
#
#
# class CommissionEmployee(SalaryEmployee):
#     def __init__(self, code, name, weekly_salary, commission):
#         super().__init__(code, name, weekly_salary)
#         self.commission = commission
#
#     def calculate_payroll(self):
#         fixed = super().calculate_payroll()
#         return fixed + self.commission
#
#
# class PayrollSystem:
#     def calculate(self, employees):
#         print("Расчёт заработной платы")
#         print("=" * 50)
#         for employee in employees:
#             print(f"Заработная плата: {employee.code} - {employee.name}")
#             print(f"- Проверить сумму: {employee.calculate_payroll()}")
#
#
# salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
# hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
# commission_employee = CommissionEmployee(3, "Николай Хорольский", 1000, 250)
# payroll_system = PayrollSystem()
# payroll_system.calculate([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])


# Упаковка данных, сериализация, десериализация
# marshal, pickle, json


import pickle

file_name = "basket.txt"

# shop_list = {
#     "фрукты": ("яблоки", "манго"),
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, "rb") as f:
#     shop_list2 = pickle.load(f)
#
# print(shop_list2)


class Text:
    num = 35
    string = "Привет"
    lst = [1, 2, 3]
    tpl = (22, 23)

    def __str__(self):
        return f"Число: {Text.num}\nСтрока: {Text.string}\nСписок: {Text.lst}\nКортеж: {Text.tpl}"


obj = Text()

my_obj = pickle.dumps(obj)
print(my_obj)

obj2 = pickle.loads(my_obj)
print(obj2)
