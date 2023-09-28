class Question:
    def __init__(self, text: str, answer: bool):
        self.__text = text
        self.__answer = answer

    # Getters

    @property
    def text(self):
        return self.__text

    @property
    def answer(self):
        return self.__answer

    def __repr__(self):
        return f"{self.__class__.__name__}: ({self.text}: {self.answer})"
