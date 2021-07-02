import turtle

turtle.shape('turtle')

degree = 5
distance = 0.5

while True:
    turtle.forward(distance)
    turtle.left(degree)
    distance += 0.01

turtle.mainloop()
