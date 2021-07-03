import turtle

turtle.shape('turtle')

distance = 20
n = 3

while True:
    turtle.pendown()
    for i in range(1, n + 1, 1):
        turtle.forward(distance)
        turtle.left(360/n)
    n += 1
    turtle.penup()
    turtle.right(90)
    turtle.forward(distance/2)
    turtle.left(90)
    #turtle.forward(distance)
    #turtle.left(90)
    distance *= 1.5

turtle.mainloop()
