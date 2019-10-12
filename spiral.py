import turtle

for side in range(1, 11):
    # 1, 2, 3, 4, 5, 6, 7, 8, 9
    turtle.forward(side * 10)
    turtle.left(90)

turtle.hideturtle()
turtle.exitonclick()
