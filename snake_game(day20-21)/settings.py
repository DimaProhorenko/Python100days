class Settings:
    def __init__(self):
        # Screen settings
        self.__screen_width = 600
        self.__screen_height = 600
        self.__screen_bg = "black"
        self.__screen_title = "Python game"
        # Snake settings
        self.__snake_color = "white"
        self.__snake_square_size = 20

    @property
    def screen_width(self):
        return self.__screen_width

    @property
    def screen_height(self):
        return self.__screen_height

    @property
    def screen_bg(self):
        return self.__screen_bg

    @property
    def screen_title(self):
        return self.__screen_title

    @property
    def snake_color(self):
        return self.__snake_color

    @property
    def snake_square_size(self):
        return self.__snake_square_size
