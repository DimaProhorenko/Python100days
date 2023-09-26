import random
import os

import art
import data


def clear_console():
    os.system('cls')


def display_message(name, description, country, type="a"):
    if type == "a":
        print(f"Compare A: {name}, {description}, from {country}")
    else:
        print(f"Against B: {name}, {description}, from {country}")


def display_person(person, type="a"):
    display_message(person["name"], person["description"],
                    person["country"], type)


def get_person():
    index = random.randint(0, len(data.data) - 1)
    return data.data.pop(index)


def get_user_input():
    while True:
        choice = input(
            "Who has more followers on Instagram? Type 'a' or 'b': ").lower()
        if choice == 'a' or choice == 'b':
            break
        print("Invalid input. Try again")
    return choice


def get_corrent_anser(p1, p2):
    if p1['follower_count'] > p2['follower_count']:
        return ['a', p1]
    return ['b', p2]


def loose(score):
    print("HAHAHHAHAHAHHA")
    print("You lost")
    print(f"Your final score is {score}")


def play():
    score = 0
    is_on = True
    last_person = {}
    print(art.logo)
    while is_on:
        clear_console()
        if score > 0:
            person = last_person
            print(f"Your score is {score}")
        else:
            person = get_person()
        display_person(person)
        print(art.vs)
        person2 = get_person()
        display_person(person2, "b")
        correct = get_corrent_anser(person, person2)
        print(correct)
        answer = get_user_input()

        if correct[0] == answer:
            score += 1
            last_person = correct[1]
        else:
            is_on = False
            clear_console()
            loose(score)


play()
