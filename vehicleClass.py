class Vehicle:
    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

class Bus(Vehicle):
  pass
b = Bus("bus3000" , 145 , 56)
print(b.name)
print(b.speed)
print(b.mileage)
  
     