from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(100)


s.listen()
s.onkey(key="space", fun=move_forward)

s.exitonclick()
