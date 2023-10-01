from turtle import Turtle, Screen
import random

screen_width = 500
screen_height = 400

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

s = Screen()


s.setup(screen_width, screen_height)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle do you think is gonna win?").lower()


def create_turtles():
    turtles = []
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtles.append(turtle)
        random.shuffle(turtles)
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
        if check_win(turtle):
            return turtle
    return None


def check_win(current_turtle):
    return current_turtle.xcor() >= screen_width / 2 - 40


def check_user_win(win_turtle):
    return user_bet == win_turtle.color()[0]


def start():
    turtles_list = create_turtles()
    reset_all_turtles(turtles_list)
    while True:
        winner = move_turtles(turtles_list)
        if isinstance(winner, Turtle):
            print("You won" if check_user_win(winner) else "You lost")
            break


start()
s.exitonclick()
