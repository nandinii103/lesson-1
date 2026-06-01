class Computer:
    def __init__(self):
        self.__max_price = 123456
    def sell(self):
        print(self.__max_price)
    def setMaxPrice(self,price):
        self.__max_price = price
s = Computer()
s.sell()
s.__max_price = 45689.09843437288
s.sell()
s.setMaxPrice(45689.09843437288)
s.sell()

    
        