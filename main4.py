from turtle import Turtle, Screen
import random
import moveturtle as mt

turtle = Turtle()
screen = Screen()
turtle.penup()
# turtle.hideturtle()
turtle.color("green")
turtle.pensize(1)
screen.colormode(255)

def random_color():
    r_colour = random.randint(0, 255)
    g_colour = random.randint(0, 255)
    b_colour = random.randint(0, 255)
    return r_colour, g_colour, b_colour

def move_turtle(moves):
    jump_moves = int(360/moves)
    for i in range(0,360,jump_moves):
        line_colour = random_color()
        turtle.pencolor(line_colour[0], line_colour[1], line_colour[2])
        turtle.pendown()
        turtle.setheading(i+10)
        turtle.circle(50,360,None)

turtle.speed(5)
moves_to_make = int(input("How many moves do you want to make? "))

# while move_number <= moves_to_make:
#     line_colour = random_color()
#     turtle.pencolor(line_colour[0], line_colour[1], line_colour[2])
#     move_turtle()
#     move_number += 1

move_turtle(moves_to_make)

screen.listen()
screen.exitonclick()