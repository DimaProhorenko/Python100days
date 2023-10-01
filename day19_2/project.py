from turtle import Turtle, Screen
import random

screen_width = 500
screen_height = 400

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

s = Screen()


s.setup(screen_width, screen_height)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle do you think is gonna win?")


def create_turtles():
    turtles = []
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtles.append(turtle)
    return turtles


def reset_turtle_position(turtle, y_value):
    turtle.penup()
    turtle.goto(x=-screen_width / 2 + 20, y=y_value)
    turtle.pendown()


def reset_all_turtles(turtles):
    y_location = screen_height / 2 - 20
    for turtle in turtles:
        reset_turtle_position(turtle, y_location)
        y_location -= screen_height / len(colors)


def move_turtles(turtles):
    for turtle in turtles:
        turtle.forward(random.randint(10, 30))


def check_win(turtles):
    for turtle in turtles:
        if round(turtle.xcor(), 2) >= screen_width / 2 - 40:
            turtle.setx(screen_width / 2 - 40)
            return turtle
    return None


def start():
    turtles_list = create_turtles()
    reset_all_turtles(turtles_list)
    while True:
        move_turtles(turtles_list)
        winner = check_win(turtles_list)
        if winner is not None:
            print(winner.color())
            break


start()


s.exitonclick()
