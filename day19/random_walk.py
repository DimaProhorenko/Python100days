import random
from turtle import Turtle, Screen

directions = [0, 90, 180, 270, 360]


t = Turtle()
screen = Screen()

screen.colormode(255)

t.shape("turtle")
t.speed(0)
t.width(3)


def get_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def walk():
    dir = random.choice(directions)
    t.color(get_rgb())
    t.left(dir)
    t.forward(20)


def spirograph(gap):
    for i in range(360 // gap):
        t.color(get_rgb())
        t.circle(100)
        t.setheading(t.heading() + gap)


# for i in range(0, 200):
#     walk()
spirograph(5)


screen.exitonclick()
