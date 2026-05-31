class Bird:
    def __init__(self):
        print("Bird constructor called")
    def fly(self):
        print("Birds can fly")
    def swim(self):
        print("Birds can swim")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("penguin constructor called")
    def run(self):
        print("penguin can run")
p = Penguin()
p.fly()
p.swim()
p.run()
