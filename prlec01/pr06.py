import turtle

turtle.shape('turtle')
print("Введите число лап паука: ")
n = int(input())

for i in range(0, n, 1):
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(180 + 360/n)

turtle.mainloop()
