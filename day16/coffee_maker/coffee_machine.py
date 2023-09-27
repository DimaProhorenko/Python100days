from menu import Menu, MenuItem
from art import logo
import commands
from printer import Printer
from money_machine import MoneyMachine
import os


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
            "report": self.report,
            "exit": self.exit,
            "revenue": self.show_revenue,
        }
        self.__mm = MoneyMachine()
        self.__is_running = True

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

    @property
    def mm(self):
        return self.__mm

    @property
    def is_running(self):
        return self.__is_running

    @menu_item.setter
    def menu_item(self, value):
        if type(value) == MenuItem:
            self.__menu_item = value
        else:
            print("Wrong type")

    @is_running.setter
    def is_running(self, value: bool):
        self.__is_running = value

    @total.setter
    def total(self, value):
        if value >= 0:
            self.__total = value

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
            Printer.add_row([item.capitalize(), self.ingredients[item]])
        Printer.print_table()
        Printer.clear_table()

    def exit(self):
        self.is_running = False
        os.system("cls")
        print("GOOD BYE")

    def show_revenue(self):
        print(f"Total is: ${self.total}")

    def check_enough_ingredients(self, menu_item):
        for key in self.ingredients:
            if self.ingredients[key] < menu_item.ingredients[key]:
                return False
        return True

    def make_menu_item(self):
        for key in self.ingredients:
            self.ingredients[key] -= self.menu_item.ingredients[key]
        print(f"Here's your {self.menu_item.name}")

    def operate(self, user_choice):
        if user_choice[0] == commands.MAKE_COFFEE:
            self.menu_item = user_choice[1]
            if self.check_enough_ingredients(self.menu_item):
                payment = self.mm.get_payment()
                if self.mm.check_payment(self.menu_item.price):
                    self.total += payment
                    self.make_menu_item()
            else:
                print("Not enough resources")
        else:
            user_choice[1]()

    def run(self):
        self.show_greeting()
        while self.is_running:
            self.show_menu()
            user_choice = self.get_user_choice()
            self.operate(user_choice)
