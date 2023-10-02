from settings import Settings
from turtle import Screen
from snake import Snake


class Game:
    def __init__(self):
        # Screen
        self.__settings = Settings()
        self.__screen = Screen()
        self.screen_setup()
        # Snake
        self.__snake = Snake(self.settings)

    @property
    def settings(self):
        return self.__settings

    @property
    def screen(self):
        return self.__screen

    @property
    def snake(self):
        return self.__snake

    def screen_setup(self):
        self.screen.setup(self.settings.screen_width, self.settings.screen_height)
        self.screen.bgcolor(self.settings.screen_bg)
        self.screen.title(self.settings.screen_title)

    def run(self):
        self.screen.exitonclick()

