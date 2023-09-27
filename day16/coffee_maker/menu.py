from printer import Printer


class MenuItem:
    def __init__(self, name: str, price: float, water: int, milk: int, coffee: int):
        assert price >= 0, f"price attribute: {price} -> is less than or equals to 0"

        self.__name = name.lower()
        self.__price = price
        self.__ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

    # Getters and Setters
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def ingredients(self):
        return self.__ingredients

    def compare_name(self, name):
        return self.name == name


class Menu:
    def __init__(self):
        self.__items = [
            MenuItem("Latte", 2.55, water=200, milk=150, coffee=24),
            MenuItem("Espresso", 1.5, water=50, milk=0, coffee=18),
            MenuItem("Cappuccino", 3, water=250, milk=50, coffee=24)
        ]

    # Getters

    @property
    def items(self):
        return self.__items

    def display_items(self):
        Printer.set_fields(["Coffee", "Cost"])
        for item in self.items:
            # print(f"{item.name}: ${item.price}")
            Printer.add_row([item.name.capitalize(), f"${item.price}"])
        Printer.print_table()
        Printer.clear_table()

    def check_item_exists(self, name):
        counter = 0
        for item in self.items:
            if item.compare_name(name):
                return counter
            counter += 1
        return -1

    def get_item_index(self, name):
        for item in self.items:
            if item.compare_name(name):
                return True
            break
        return False
