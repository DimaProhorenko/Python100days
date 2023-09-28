class MoneyMachine:
    def __init__(self):
        self.__total = 0

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, value):
        if value >= 0:
            self.__total = value

    def get_payment(self):
        print("Please insert coins.")
        self.total = int(input("how many quarters?: ")) * 0.25
        self.total += int(input("how many dimes?: ")) * 0.1
        self.total += int(input("how many nickles?: ")) * 0.05
        self.total += int(input("how many pennies?: ")) * 0.01
        return self.total

    def check_payment(self, cost):
        total = self.total
        self.total = 0
        if cost == total:
            return True
        elif cost < total:
            print(f"Here's your change: ${round(total - cost, 2)}")
            return True
        print(f"Not enough money. You have been refunded ${total}")
        return False
