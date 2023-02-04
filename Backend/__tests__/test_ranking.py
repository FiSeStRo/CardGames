from Backend import definitions
from Backend.ranking import calculate_hand_value


def test_calculate_hand_value():
    assert calculate_hand_value() == definitions.RANK_HIGH_CARD
