import random
import helpers
import constants
import art


difficulty_type = {
    "easy": constants.EASY_ATTEMPTS,
    "hard": constants.HARD_ATTEMPTS,
}


def get_difficulty():
    difficulty = ""
    while not difficulty in difficulty_type:
        difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
    return difficulty_type[difficulty]


def choose_num():
    return random.randint(constants.MIN_NUM, constants.MAX_NUM)


def make_guess():
    return int(input("Make a guess: "))


def check_guess(guess, num):
    if guess == num:
        return True
    return False


def higher_lower(guess, num):
    if guess > num:
        return "Too high"
    return "Too low"


def display_heading():
    helpers.clear_console()
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")


def display_winning():
    print(art.win)
    print("Congrats. You have won")


def display_loose():
    print(art.loose)
    print("You have lost")


def get_play():
    again = True

    while True:
        choice = input("Wanna play? Type 'y' or 'n': ")
        if choice == "y":
            break
        if choice == "n":
            again = False
            break
        elif choice != "y":
            print("Unknown command. Probably a typo")

    return again


def play():
    display_heading()
    attempts = get_difficulty()
    guessed_num = choose_num()
    guess = 0
    is_win = False

    while guess != guessed_num and attempts > 0:
        print(f"You have {attempts} attempts left")
        guess = make_guess()
        if check_guess(guess, guessed_num):
            print("You did it!")
            is_win = True
            break
        else:
            print(higher_lower(guess, guessed_num))
        attempts -= 1

    if is_win:
        display_winning()
    else:
        display_loose()


def game():

    while True:
        is_playing = get_play()
        if is_playing:
            play()
        else:
            break


game()
