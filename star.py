import turtle

def star_5():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)
        turtle.forward(100)
        turtle.left(72)

def star_6():
    for _ in range(6):
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.left(60)

star_5()

turtle.exitonclick()
