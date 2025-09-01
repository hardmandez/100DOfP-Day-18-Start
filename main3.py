from turtle import Turtle, Screen
import random
import moveturtle as mt

turtle = Turtle()
screen = Screen()
turtle.shape("turtle")
turtle.color("green")
turtle.pensize(15)
screen.colormode(255)

def random_color():
    r_colour = random.randint(0, 255)
    g_colour = random.randint(0, 255)
    b_colour = random.randint(0, 255)
    return r_colour, g_colour, b_colour

def move_forward():
    turtle.forward(40)

def move_backward():
    turtle.left(180)
    turtle.forward(40)
def move_left():
    turtle.left(90)
    turtle.forward(40)

def move_right():
    turtle.right(90)
    turtle.forward(40)

def move_turtle():
    action = [move_forward, move_backward, move_left, move_right]
    random.choice(action)()

turtle.speed(1)
move_number = 0
moves_to_make = int(input("How many moves do you want to make? "))

while move_number <= moves_to_make:
    line_colour = random_color()
    turtle.pencolor(line_colour[0], line_colour[1], line_colour[2])
    move_turtle()
    move_number += 1


screen.listen()
screen.exitonclick()