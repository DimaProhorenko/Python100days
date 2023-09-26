MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def check_ingredients(coffee):
    ingredients = coffee['ingredients']
    is_enough = True
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            is_enough = False
            break
    return is_enough


def show_ingredient_insuficient():
    print("Sorry we can't make your coffee. Not enough ingredients")


def get_user_input_coffee():
    while True:
        user_input = input(
            f"What would you like? ({','.join(MENU.keys())}): ").lower()
        if user_input == "q":
            return "exit"
        if user_input == "report":
            show_report()
            continue
        if user_input not in MENU:
            print(
                f"Sorry we don't have {user_input} in menu. It's probably a typo")
        else:
            break
    return {"name": user_input, **MENU[user_input]}


def make_coffee(coffee):
    ingredients = coffee["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here's your {coffee['name']}")


def show_total_price(coffee):
    print(f"Your total is ${coffee['cost']}")


def show_report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_payment(total_payed, cost):
    if total_payed < cost:
        print(f"Sorry, that's not enough money. ${total_payed} refunded!")
        return False
    else:
        global profit
        profit += cost
        if total_payed == cost:
            print("Payment accepted!")
        else:
            print(f"Here's ${round(total_payed - cost, 2)} in change")
        return True


def run():
    is_on = True

    while is_on:
        coffee = get_user_input_coffee()
        if coffee == "exit":
            is_on = False
            break
        is_enough_ingredients = check_ingredients(coffee)
        if is_enough_ingredients:
            show_total_price(coffee)
            payment = process_coins()
            payment_successfull = check_payment(payment, coffee["cost"])
            if payment_successfull:
                make_coffee(coffee)
        else:
            show_ingredient_insuficient()


run()
