import turtle

turtle.shape('turtle')
for i in range(5, 51, 5):
    turtle.pendown()
    for j in range(0, 4):
        turtle.forward(10 + i*5)
        turtle.left(90)
    turtle.penup()
    turtle.backward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

turtle.mainloop()
