import turtle
import math

def polygon(n, side):
    turtle.begin_fill()
    for _ in range(n):
        turtle.forward(side)
        turtle.left(180 - (n-2)*180/n)
    turtle.end_fill()

turtle.tracer(0)
turtle.right(90)
turtle.up()
turtle.forward(300)
turtle.left(90)
turtle.down()
for i in range(100, 3, -1):
    turtle.color(
        (math.sin(i/100*2*math.pi)+1)/2,
        (math.sin((i+33)/100*2*math.pi)+1)/2,
        (math.sin((i+66)/100*2*math.pi)+1)/2)
    polygon(i, 20)
turtle.hideturtle()
turtle.update()

turtle.exitonclick()
