import deck


def get_card(my_deck, hand):
    hand.append(deck.deal_card(my_deck))
