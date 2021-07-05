import turtle

turtle.shape('turtle')

distance = 1
n = 3
turtle.speed(10)

def cycle(turn):
    for i in range(1, 361, 2):
        if turn:
            turtle.left(2)
        else:
            turtle.right(2)
        turtle.forward(distance)

while n:
    turn = True
    cycle(turn)
    turn = not(turn)
    cycle(turn)
    turtle.left(360 / 3)
    n -= 1


turtle.mainloop()
