class BMW:
    def brand(self):
        print("BMW")
class Ferrari:
    def brand(self):
        print("Ferrari")

car1 = BMW()
car2 = Ferrari()

for car in (car1,car2):
    car.brand()