class Employee:
    def __init__(self, code, name):
        self.code = code
        self.name = name


class SalaryEmployee(Employee):
    """Административные работники, имеющие фиксированную зарплату"""
    def __init__(self, code, name, weekly_salary):
        super().__init__(code, name)
        self.ws = weekly_salary

    def calculate_payroll(self):
        return self.ws


class HourlyEmployee(Employee):
    """Сотрудники, имеющие почасовую зарплату"""
    def __init__(self, code, name, time, rate_per_hour):
        super().__init__(code, name)
        self.time = time
        self.rph = rate_per_hour

    def calculate_payroll(self):
        return self.time * self.rph


class CommissionEmployee(SalaryEmployee):
    def __init__(self, code, name, weekly_salary, commission):
        super().__init__(code, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
