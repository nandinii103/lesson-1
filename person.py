class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name)
        print(self.id)

class Employee(Person):
    def __init__(self, name, id , salary, post):
        super().__init__(name, id)
        self.salary = salary
        self.post = post
e = Employee("Bob",456,25400935673, "idk" )
e.display()
print(e.salary)
print(e.post)

    


