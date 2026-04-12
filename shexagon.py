import turtle

screen = turtle.Screen()
screen.bgcolor = ("blue")
screen.setup(400 , 500)
pen = turtle.Turtle()
num_sides = 6
side_length = 100
angle = 360/num_sides

for i in range(num_sides):
    pen.forward(side_length)
    pen.right(angle)
turtle.done()
    