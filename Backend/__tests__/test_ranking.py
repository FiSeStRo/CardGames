from Backend import definitions
from Backend.ranking import calculate_hand_value_str


def test_calculate_hand_value():
    str_rubbish_hand = "23s69c7Th5d"
    assert calculate_hand_value_str(str_rubbish_hand) == definitions.RANK_HIGH_CARD
