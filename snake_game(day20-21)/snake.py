from turtle import Turtle
from settings import Settings


class Snake:
    def __init__(self, settings: Settings):
        self.__settings = settings
        self.__snake = Turtle()
        self.set_props(self.snake)
        self.__body = [self.snake]
        # self.__direction = ""
        self.create_square()
        self.create_square()

    @property
    def snake(self):
        return self.__snake

    @property
    def settings(self):
        return self.__settings

    @property
    def body(self):
        return self.__body

    def set_props(self, square):
        square.color(self.settings.snake_color)
        square.shape("square")
        square.penup()

    def get_square_position(self):
        return self.body[-1].xcor() + self.settings.snake_square_size

    def create_square(self):
        square = Turtle()
        self.set_props(square)
        square.setx(self.get_square_position())
        self.body.append(square)

    # def move(self):


