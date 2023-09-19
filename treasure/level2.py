import random
import level3
choices = ["You were eaten by an unknown creature",
           "Something dragged you underwater", "Continue"]


def start():
    input("You are standing in front of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim: ")
    result = choices[random.randint(0, len(choices) - 1)]
    if result == "Continue":
        level3.start()
    else:
        print(result)
