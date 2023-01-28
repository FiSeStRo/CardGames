import definitions
import random


def create_deck(shuffle=True):
    shuffle_array = [i for i in range(definitions.NUM_CARDS_PER_DECK)]
    if shuffle:
        random.shuffle(shuffle_array)
    return shuffle_array
