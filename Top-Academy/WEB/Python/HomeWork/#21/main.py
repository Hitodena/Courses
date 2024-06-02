class Vehicle:
    
    def __init__(self, company, model, hp, year, color, price):
        self.company = company
        self.model = model
        self.hp = hp
        self.year = year
        self.color = color
        self.price = price
    
    def print_data(self):
        print(" Vehicle Data ".center(40, "*"))
        print(f"Company: {self.company}\nModel: {self.model}\nHP: {self.hp}\nYear: {self.year}\nColor: {self.color}\nPrice: {self.price}")
        print("=" * 40)
    
    def get_company(self):
        print(f"Производитель: {self.company}")
        
    def get_model(self):
        print(f"Модель: {self.model}")
        
    def get_hp(self):
        print(f"Мощность двигателя: {self.hp}")
        
    def get_year(self):
        print(f"Год выпуска: {self.year}")
        
    def get_color(self):
        print(f"Цвет: {self.color}")
        
    def get_price(self):
        print(f"Цена: {self.price}")
        
    def set_company(self, company):
        self.company = company
        
    def set_model(self, model):
        self.model = model
        
    def set_hp(self, hp):
        self.hp = hp
        
    def set_year(self, year):
        self.year = year
        
    def set_color(self, color):   
        self.color = color
        
    def set_price(self, price):
        self.price = price
        

car = Vehicle("Dodge", "Charger", 233, 1969, "Black", "84.900$")
car.print_data()

car.set_model("Challenger Hellcat")
car.set_hp(729)
car.set_year(2015)
car.set_price("142.000$")
car.print_data()