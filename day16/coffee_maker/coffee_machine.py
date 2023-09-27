from menu import Menu, MenuItem
from art import logo
import commands
from printer import Printer


class CoffeeMachine:
    def __init__(self):
        self.__total = 0
        self.__ingredients = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.menu = Menu()
        self.__menu_item = None
        self.__commands = {
            "report": self.report
        }
        self.__command = ""

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

    @property
    def menu_item(self):
        return self.__menu_item

    @property
    def command(self):
        return self.__command

    @menu_item.setter
    def menu_item(self, value):
        if type(value) == MenuItem:
            self.__menu_item = value
        else:
            print("Wrong type")

    @command.setter
    def command(self, value):
        self.__command = value

    def show_greeting(self):
        print("Welcome to PyCoffee.")
        print(logo)

    def show_menu(self):
        self.menu.display_items()

    def get_user_choice(self):
        while True:
            choice = input("What would you like?: ").lower()
            index = self.menu.check_item_exists(choice)
            if index > -1:
                return [commands.MAKE_COFFEE, self.menu.items[index]]
            else:
                if choice in self.commands:
                    return [commands.TECH, self.commands[choice]]
                else:
                    print("Unknown command. Probably a typo.")

    def report(self):
        Printer.set_fields(["Ingredient", "Amount"])
        for item in self.ingredients:
            # print(f"{item}: {self.ingredients[item]}")
            Printer.add_row([item.capitalize(), self.ingredients[item]])
        Printer.print_table()
        Printer.clear_table()

    def check_enough_ingredients(self, menu_item):
        for key in self.ingredients:
            if self.ingredients[key] < menu_item.ingredients[key]:
                return False
        return True

    def make_menu_item(self):
        for key in self.ingredients:
            self.ingredients[key] -= self.menu_item.ingredients[key]

    def operate(self, user_choice):
        if user_choice[0] == commands.MAKE_COFFEE:
            self.menu_item = user_choice[1]
            if self.check_enough_ingredients(self.menu_item):
                self.make_menu_item()
                self.report()
            else:
                print("Not enough resources")
        else:
            user_choice[1]()

    def run(self):
        self.show_greeting()
        self.show_menu()
        user_choice = self.get_user_choice()
        self.operate(user_choice)
