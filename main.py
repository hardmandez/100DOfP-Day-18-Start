from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.color("green")
turtle.pencolor("black")
turtle.shape("turtle")

# timmy_the_turtle.listen()
#
# timmy_the_turtle.onkey(forward,"Up")
turtle.speed(1)
for i in range(4):
    turtle.forward(100)
    turtle.left(90)





screen.exitonclick()