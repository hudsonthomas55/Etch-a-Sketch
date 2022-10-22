from turtle import Turtle, Screen

# Name turtle and screen
sheldon = Turtle()
sheldon.shape("turtle")
sheldon.speed("fastest")
screen = Screen()


# Functions for turtle directions:
def move_forward():
    sheldon.fd(10)


def move_backward():
    sheldon.back(10)


def turn_left():
    new_heading = sheldon.heading() + 10
    sheldon.setheading(new_heading)


def turn_right():
    new_heading = sheldon.heading() - 10
    sheldon.setheading(new_heading)


def clear():
    sheldon.clear()
    sheldon.penup()
    sheldon.home()
    sheldon.pendown()


# Screen commands. Listen and direct Sheldon.
screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="space", fun=clear)

screen.exitonclick()