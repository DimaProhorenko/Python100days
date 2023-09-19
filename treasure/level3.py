import random


def start():
    color = input("You got to shore in one peace and got inside a cave for the night. Once inside you discovered 3 doors. Type 'red' to open red door, 'blue' to open blue door, 'green' to open green door: ")
    choices = [f"Behind the {color} door was huge dragon. It ate you alive!", f"Behind the {color} door was some kind of creature. It lurked you inside. You fell asleep and never woke up!",
               f"Behind the {color} door was darkness. You walked inside and saw a little glimpse of light. It was growing. It scared you, but the door was already closed. You died a painfull death", "Continue"]
    result = choices[random.randint(0, len(choices) - 1)]
    if result == "Continue":
        print("YEEEEEAAAAAAAAAAHHH\nYou have found the treasure")
    else:
        print(result)
