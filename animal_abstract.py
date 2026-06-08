from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("move")

class Dog(Animal):
    def move(self):
        print("animal")

dog = Dog()
human = Human()

dog.move()
human.move()