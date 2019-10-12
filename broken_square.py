import turtle

def broken_square(side, gap):
    for _ in range(4):
        turtle.forward((side-gap) / 2)
        turtle.up()
        turtle.forward(gap)
        turtle.down()
        turtle.forward((side-gap) / 2)
        turtle.right(90)

broken_square(200, 100)

turtle.exitonclick()
