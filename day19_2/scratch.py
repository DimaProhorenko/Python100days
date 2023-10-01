from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def rotate_right():
    t.setheading(t.heading() + 10)


def rotate_left():
    t.setheading(t.heading() - 10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=rotate_left)
s.onkey(key="d", fun=rotate_right)
s.onkey(key="space", fun=clear)

s.exitonclick()