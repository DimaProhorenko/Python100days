import os
from logo import logo

bids = []


def welcome():
    print(logo)
    print("Welcome to the secret auction program.")


def get_user_bid():
    name = input("Enter you name: ")
    bid = float(input("Enter your bid: "))
    bids.append({"name": name, "bid": bid})


def get_highest_bid():
    highest_bid = 0
    bidder = {}
    for person in bids:
        current_bid = person["bid"]
        if current_bid > highest_bid:
            highest_bid = current_bid
            bidder["name"] = person["name"]
            bidder["bid"] = current_bid
    return bidder


def clear_screen():
    os.system("cls")


def print_result(bidder):
    clear_screen()
    print(logo)
    print(f"The winner is {bidder['name']} with a bid of ${bidder['bid']}")


def play():
    while True:
        get_user_bid()
        more_users = input("Are there any other bidders? Type y/n: ")
        if more_users == "n":
            # print(get_highest_bid())
            print_result(get_highest_bid())
            break
        clear_screen()


is_program_on = True

while is_program_on:
    clear_screen()
    welcome()
    play()
    next_auction = input("Next auction? Type y/n: ")
    if next_auction == "n":
        clear_screen()
        print("Bye")
        break
