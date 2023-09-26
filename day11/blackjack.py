import logo
import deck as my_deck
import helpers
import bot

player_hand = []
comp_hand = []
has_lost = False


def reset_hand(hand):
    hand = []


def reset():
    global player_hand
    global comp_hand
    player_hand = []
    comp_hand = []


def first_round(deck):
    for i in range(0, 2):
        player_hand.append(my_deck.deal_card(deck))
        comp_hand.append(my_deck.deal_card(deck))
    display_hand(player_hand)
    display_hand(comp_hand, False)


def draw_card(hand, deck):
    is_deal = True
    while is_deal:
        choice = input("Type 'y' to get another card, type 'n' to pass:")
        if choice == "y":
            card = my_deck.deal_card(deck)
            hand.append(card)
            display_hand(hand)
            if check_loose(hand):
                is_deal = False
        elif choice == "n":
            print(
                f"Your final hand is {hand}, total - {count_total(hand)}")
            is_deal = False
        else:
            print("Unknown choice. Probably a typo")


def count_total(hand):
    total = 0
    for card in hand:
        total += my_deck.get_card_value(card)
    return total


def display_hand(hand, is_player=True, show_all=False):
    total = count_total(hand)
    if is_player:
        print(f"Your cards {hand}, current score: {total}")
    else:
        if show_all:
            print(f"Computer hand: {hand}, current score: {total}")
        else:
            print(f"Computer first card: {hand[0]}")


def display_comp_hand(show_all):
    display_hand(comp_hand, False, show_all)


def comp_choice(deck):
    while True:
        total = count_total(comp_hand)
        if total >= 19:
            break
        bot.get_card(deck, comp_hand)
        display_comp_hand(True)


def check_loose(hand):
    total = count_total(hand)
    if total > 21:
        return True
    return False


def get_winner():
    player_count = count_total(player_hand)
    comp_count = count_total(comp_hand)

    if player_count > 21:
        print("You lost")
    elif comp_count > 21:
        print("You won")
    elif player_count < comp_count:
        print("You lost")
    elif player_count > comp_count:
        print("You won")
    elif player_count == comp_count:
        print("It's a draw")
    elif player_count == 21:
        print("You won")
    elif comp_count == 21:
        print("You lsot")


def play():
    reset()
    helpers.clear_console()
    print(logo.logo)
    deck = my_deck.shuffle_deck(my_deck.get_deck())
    first_round(deck)
    draw_card(player_hand, deck)
    display_comp_hand(True)
    comp_choice(deck)
    get_winner()


while True:
    start = input("Wanna play blackjack? Enter y/n: ").lower()
    if start == "n":
        break
    play()
