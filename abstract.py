from abc import ABC, abstractmethod

class Base(ABC):
    def display(self):
        print("bdejfhwifh")
    @abstractmethod
    def show(self):
        pass

class Child(Base):
    def show(self):
        print("I like food")
child = Child()

child.display()
child.show()


    
