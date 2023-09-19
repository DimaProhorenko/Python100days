import random
import level2

choices = [
    "A huge black bear was around the corner. You have been ripped appart.", "Continue"]


def start():
    print("Welcome, traveler!")
    choice = input(
        "You are standing at a crossroad. Type 'left' to go left. Type 'right' to go right: ")
    result = choices[random.randint(0, 1)]
    if result == "Continue":
        level2.start()
    else:
        print(result)
