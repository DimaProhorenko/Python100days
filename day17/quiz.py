from data import question_data
from question import Question


class Quiz:
    def __init__(self):
        self.__bank = self.initialize_bank()
        self.__current_question = 0
        self.__score = 0

    @property
    def bank(self):
        return self.__bank

    @property
    def current_question(self):
        return self.__current_question

    @current_question.setter
    def current_question(self, value):
        if value > self.current_question or value == 0:
            self.__current_question = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value > self.score or value == 0:
            self.__score = value

    def initialize_bank(self):
        q_list = []
        for q in question_data:
            q_list.append(Question(q['text'], q['answer']))
        return q_list

    def next_question(self):
        print("")
        while True:
            answer = input(
                f"Q{self.current_question + 1}: {self.bank[self.current_question].text}. (True/False)?: ").capitalize()
            if answer == "True" or answer == "False":
                return answer

    def check_answer(self, answer):
        return self.bank[self.current_question].answer == answer

    def display_score(self):
        print(f"Oh yeaaaah. Here's your score: {self.score}")

    def run(self):
        bank_length = len(self.bank)

        while self.current_question < bank_length - 1:
            answer = self.next_question()
            if (self.check_answer(answer)):
                self.score += 1
            self.current_question += 1
        self.display_score()
