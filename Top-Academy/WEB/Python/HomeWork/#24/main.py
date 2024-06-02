class Student:
    def __init__(self, name):
        self.name = name
        self.lp = self.Laptop

    def print_info(self):
        print(f"{self.name} => {self.lp.brand}, {self.lp.cpu}, {self.lp.ram}")

    class Laptop:
        brand = "HP"
        cpu = "i7"
        ram = "16"


r = Student("Roman")
r2 = Student("Vladimir")
r.print_info()
r2.print_info()
