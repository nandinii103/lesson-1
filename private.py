class Nandinii:
    def __init__(self):
        self.__privateVar = 45
    def __privMeth(self):
        print("OOP are bad")
    def display(self):
        print(self.__privateVar)
        self.__privMeth()
d = Nandinii()
d.display()
