from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.color("green")
turtle.pencolor("black")
turtle.shape("turtle")


def move_forward():
    for _ in range(10):
        turtle.pendown()
        turtle.forward(2)
        turtle.penup()
        turtle.forward(2)

def move_backward():
    turtle.left(180)

def move_left():
    turtle.left(90)

def move_right():
    turtle.right(90)

# def pen_status(pen_state):
#         if pen_state == True:
#             return False
#         else:
#             return True

def game_reset():
    turtle.reset()
