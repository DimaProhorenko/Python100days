print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to treasure island!!!")
print("Your mission is to find treasure")
choice1 = input(
    "You are at a crossroad. Where do you wanna go next? (left/ right)").lower()

if choice1 == "left":
    choice2 = input(
        "You are at a lake. There's an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across").lower()
    if choice2 == "wait":
        choice3 = input(
            "You came to shore in one peace. There are two doors. Type 'first' to go through first one. Type 'second' to go through second one").lower()
        if choice3 == "first":
            print("A huge dragon was behind that door. You died!")
        else:
            print("You found the treasure!!!")
    else:
        choice4 = input(
            "You started swimming across the lake. You felt something touched your leg. Type 'back' to swim back. Type 'swim' to keep swimming.").lower()
        print("You were swallowed whole.")
else:
    print("A huge bear was around the corner. You were ripped appart")
