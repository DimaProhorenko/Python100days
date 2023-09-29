from turtle import Turtle, Screen

figures = [
    {
        "name": "triangle",
        "sides": 3
    },
    {
        "name": "square",
        "sides": 4
    },
    {
        "name": "pentagon",
        "sides": 5
    },
    {
        "name": "hexagon",
        "sides": 6
    },
    {
        "name": "heptagon",
        "sides": 7
    },
    {
        "name": "octagon",
        "sides": 8
    },
    {
        "name": "nonagon",
        "sides": 9
    },
    {
        "name": "decagon",
        "sides": 10
    }
]

t = Turtle()
screen = Screen()
t.shape("turtle")


for fig in figures:
    deg = 360 / fig["sides"]
    for i in range(0, fig["sides"]):
        t.forward(100)
        t.left(deg)


screen.exitonclick()
