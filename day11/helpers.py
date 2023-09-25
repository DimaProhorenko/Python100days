import random
import os


def get_random_int(min, max):
    return random.randint(min, max)


def clear_console():
    os.system('cls')
