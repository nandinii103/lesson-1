class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return  f"point({self.x} , {self.y})"
s = Point(10,20)
print(s)
        