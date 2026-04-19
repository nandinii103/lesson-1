import turtle

screen = turtle.Screen()
screen.bgcolor("pink")
pen = turtle.Turtle()
side_length = 100

for i in range(4):
    pen.forward(side_length)
    pen.right(90)

turtle.done()