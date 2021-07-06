import turtle

turtle.shape('turtle')
turtle.left(90)
distance = 5
turtle.speed(0)


def cycle(turn):
    for i in range(1, 180, 3):
        turtle.right(3)
        if turn:
            turtle.forward(distance)
        else:
            turtle.forward(distance / 5)


while True:
    turn = True
    cycle(turn)
    turn = not turn
    cycle(turn)


turtle.mainloop()
