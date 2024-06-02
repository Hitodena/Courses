class PayrollSystem:
    @staticmethod
    def calculate(employees):
        print("Расчёт заработной платы")
        print("=" * 50)
        for employee in employees:
            print(f"Заработная плата: {employee.code} - {employee.name}")
            print(f"- Проверить сумму: {employee.calculate_payroll()}\n")
