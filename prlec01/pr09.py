import turtle
import math

turtle.shape('turtle')
turtle.left(90)
n = 3
distance = 30
turtle.speed(2)


def polygon(n, distance):
    for i in range(1, n + 1, 1):
        turtle.left(360 / n)
        turtle.forward(distance)


while True:
    turtle.pendown()
    polygon(n, distance)
    turtle.penup()
    radius_out = distance / (2 * math.sin(math.pi / n))
    n += 1
    radius_in = distance / (2 * math.tan(math.pi / n))
    distance = 2 * radius_out * math.tan(math.pi / n)
    turtle.right(45)
    turtle.forward(10)
    turtle.left(45)



turtle.mainloop()
