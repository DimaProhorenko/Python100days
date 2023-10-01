class Settings:
    def __init__(self):
        self.__screen_width = 600
        self.__screen_height = 600
        self.__screen_bg = "black"
        self.__screen_title = "Python game"

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

