import turtle

screen = turtle.Screen()
screen.bgcolor("pink")
pen = turtle.Turtle()
size = 20
for i in range(20):
    pen.forward(size)
    pen.right(90)
    size += 10

turtle.done()