class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @name.deleter    
    def name(self):
        print("Name has been deleted.")
        del self.__name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
    
    @age.deleter
    def age(self):
        print("Age has been deleted")
        del self.__age
        

pr = Person("William", 32)
print(pr.__dict__)
print(pr.name, pr.age)
pr.name = "Frenchie"
pr.age = 28
print(pr.__dict__)
print(pr.name, pr.age)
del pr.age
print(pr.__dict__)
