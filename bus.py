class Vehicle:
    def __init__(self , brand):
        self.brand = brand

    def display(self):
        print("Vehicle Brand is" ,self.brand)
class Car(Vehicle):
    def __init__(self, brand , model):
        super().__init__(brand)
        self.model = model
    def display(self):
        print("car brand" , self.brand)
        print("car model" , self.model)

car1 = Car("merecedes" ,"C63S")
car1.display()
print("car inherits form vehicle")