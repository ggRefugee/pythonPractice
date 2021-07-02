import turtle

turtle.shape('turtle')
for i in range(0, 10, 1):
    turtle.pendown()
    for j in range(0, 4):
        turtle.forward(40 + 2*i*10)
        turtle.left(90)
    turtle.penup()
    turtle.backward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

turtle.mainloop()
