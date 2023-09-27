from menu import Menu
from art import logo


class CoffeeMachine:
    def __init__(self):
        self.__total = 0
        self.__ingredients = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.menu = Menu()
        self.__commands = {
            "report": self.report
        }

    # Getters

    @property
    def total(self):
        return self.__total

    @property
    def ingredients(self):
        return self.__ingredients

    @property
    def commands(self):
        return self.__commands

    def show_greeting(self):
        print("Welcome to PyCoffee.")
        print(logo)

    def show_menu(self):
        self.menu.display_items()

    def get_user_choice(self):
        while True:
            choice = input("What would you like?: ").lower()
            if choice in self.commands:
                self.commands[choice]()
                break
            elif self.menu.check_item_exists(choice):
                print("Proceed to make coffee")
                break
            else:
                print("Unknown command. Probably a typo!")

    def report(self):
        print("REPORT")

    def run(self):
        self.show_greeting()
        self.show_menu()
        self.get_user_choice()
