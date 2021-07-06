import turtle

turtle.shape('turtle')
turtle.left(90)
distance = 1
turtle.speed(0)


def cycle(turn):
    for i in range(1, 361, 3):
        if turn:
            turtle.left(3)
        else:
            turtle.right(3)
        turtle.forward(distance)


while True:
    turn = True
    cycle(turn)
    turn = not turn
    cycle(turn)
    distance += 0.1

turtle.mainloop()
