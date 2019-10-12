import turtle

turtle.left(90)
turtle.forward(200)
for branch in range(1, 11):
    turtle.left(135)
    turtle.forward(branch * 10)
    turtle.backward(branch * 10)
    turtle.left(90)
    turtle.forward(branch * 10)
    turtle.backward(branch * 10)
    turtle.left(135)
    turtle.backward(10)

turtle.hideturtle()
turtle.exitonclick()
