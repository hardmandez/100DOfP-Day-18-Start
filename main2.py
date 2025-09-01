from turtle import Turtle, Screen
import random
import moveturtle as mt

turtle = Turtle()
screen = Screen()
turtle.color("green")
turtle.pencolor("black")
turtle.shape("turtle")
screen.colormode(255)

def move_turtle(user_max_sides):
    no_of_side = user_max_sides
    turn_angle = 360 / no_of_side
    for i in range(no_of_side):
        turtle.forward(40)
        turtle.left(turn_angle)
    no_of_side += 1
    return no_of_side

start_no_of_side = 3
max_no_of_side = int(input("How many side do you want?"))


turtle.speed(100)
while start_no_of_side <= max_no_of_side:
    r_colour = random.randint(0, 255)
    g_colour = random.randint(0, 255)
    b_colour = random.randint(0, 255)
    turtle.pencolor(r_colour, g_colour, b_colour)
    start_no_of_side = move_turtle(start_no_of_side)


screen.listen()
screen.exitonclick()