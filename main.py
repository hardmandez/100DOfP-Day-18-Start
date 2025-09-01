from turtle import Turtle, Screen
import moveturtle as mt

turtle = Turtle()
screen = Screen()



turtle.speed(1)

screen.listen()
screen.onkey(mt.move_forward, "Up")
screen.onkey(mt.move_backward, "Down")
screen.onkey(mt.move_left, "Left")
screen.onkey(mt.move_right, "Right")
# set_pen_status = screen.onkey(pen_status(), "p")
screen.onkey(mt.game_reset, "space")

screen.exitonclick()