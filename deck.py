import definitions
import random


def create_deck():
    deck = [definitions.PID_IN_DECK_CARD for i in range(definitions.NUM_CARDS_PER_DECK)]
    return deck


def create_shuffle_array():
    shuffle_array = [i for i in range(definitions.NUM_CARDS_PER_DECK)]
    random.shuffle(shuffle_array)
    return shuffle_array
