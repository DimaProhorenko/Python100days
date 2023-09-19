import random


def print_paper():
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')


def print_rock():
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')


def print_scissors():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')


def draw(c):
    if c == "rock":
        print_rock()
    elif c == "paper":
        print_paper()
    else:
        print_scissors()


def get_result(c1, c2):
    if c1 == c2:
        return "It's a draw"
    elif (((c1 - c2 + 3)) % 3 == 1):
        return "Player won!"
    return "Computer won"


choices = ["rock", "paper", "scissors"]

while True:
    play = input("Wanna play? (y/n): ")
    if play == "n":
        break
    else:
        print("Welcome to Rock Paper Scissors")
        player_choice = int(
            input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
        computer_choice = random.randint(0, len(choices) - 1)
        draw(choices[player_choice])
        print("Computer chose: ")
        draw(choices[computer_choice])
        print(get_result(player_choice, computer_choice))
