import random
import helpers

values = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}


def get_deck():
    deck = []
    for key in values:
        for face in range(0, 4):
            deck.append(key)
    return deck


def shuffle_deck(deck):
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled


def deal_card(deck):
    return deck.pop(helpers.get_random_int(0, len(deck) - 1))


def get_card_value(card):
    return values[card]
