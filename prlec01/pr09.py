import turtle
import math

turtle.shape('turtle')

n = 3
distance = 30
radius = distance / (math.pi / n)

turtle.speed(2)
#turtle.left(90 / n)

def polygon(n, distance):
    turtle.left(90 / n)
    for i in range(1, n + 1, 1):
        turtle.left(360 / n)
        turtle.forward(distance)


while n < 6:
    turtle.pendown()
    polygon(n, distance)
    n += 1
    turtle.penup()
    radius = distance / (math.pi / n)
    distance += radius / 3
    turtle.left(90 - 90 / n)
    turtle.right(90 / n)
    turtle.forward(10)
    turtle.left(90)


turtle.mainloop()
