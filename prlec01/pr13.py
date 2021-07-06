import turtle
import math

turtle.shape('turtle')
turtle.speed(0)


def cycle(radius, color):
    turtle.begin_fill()
    for i in range(1, 360, 3):
        turtle.left(3)
        turtle.forward(2 * radius * math.sin(math.pi / 120))
    turtle.fillcolor(color)
    turtle.end_fill()
    turtle.color('black')

def half_cycle(radius, color):
    for i in range(1, 180, 5):
        turtle.left(5)
        turtle.forward(2 * (radius * 0.7) * math.sin(math.pi / 120))
    turtle.color(color)


radius = 200
turtle.left(90)
cycle(radius, 'yellow')
turtle.penup()
turtle.left(90)
turtle.forward(radius)
turtle.right(90)
turtle.forward(radius / 3)
turtle.left(90)
turtle.forward(2 * radius / 6)
turtle.right(90)
turtle.pendown()
cycle(radius / 10, 'blue')

turtle.penup()
turtle.right(90)
turtle.forward(5 * radius / 6)
turtle.left(90)
turtle.pendown()
cycle(radius / 10, 'blue')

turtle.penup()
turtle.left(90)
turtle.forward(3 * radius / 6)
turtle.left(90)
turtle.forward(radius / 6)
turtle.pendown()
turtle.color('black')
turtle.width(5)
turtle.forward(radius / 3)

turtle.penup()
turtle.forward(radius / 10)
turtle.right(90)
turtle.forward(3 * radius / 7)
turtle.left(90)
turtle.width(10)
turtle.pendown()
turtle.color('red')
half_cycle(radius, 'black')







turtle.mainloop()