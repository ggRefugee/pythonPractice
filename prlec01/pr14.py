import turtle

turtle.shape('turtle')
turtle.speed(3)
turtle.left(90)
radius = 30

def star(n, radius):
    for i in range(1, n+1, 1):
        turtle.forward(radius)
        turtle.left(90 + (180 / (2 * n)))


turtle.penup()
turtle.left(90)
turtle.forward(5 * radius)
turtle.right(90)
turtle.pendown()
turtle.left(90)
star(5, radius)

"""turtle.penup()
turtle.right(90)
turtle.forward(3 * radius)
turtle.left(90)
turtle.pendown()
star(11, radius)"""



turtle.mainloop()