from Backend import definitions
from Backend.ranking import calculate_hand_value_str


def test_check_ranking_high_card():
    hand = '23s69c7Th5d'
    assert calculate_hand_value_str(hand) == definitions.RANK_HIGH_CARD


def test_check_ranking_one_pair():
    hand = '23s69c7Th3d'
    assert calculate_hand_value_str(hand) == definitions.RANK_ONE_PAIR


def test_check_ranking_two_pair():
    hand = '23s23c7Th5d'
    assert calculate_hand_value_str(hand) == definitions.RANK_TWO_PAIR


def test_check_ranking_three_of_a_kind():
    hand = '23s3c3Th57d'
    assert calculate_hand_value_str(hand) == definitions.RANK_THREE_OF_A_KIND


def test_check_ranking_straight():
    hand = '23s4c5Th67d'
    assert calculate_hand_value_str(hand) == definitions.RANK_STRAIGHT


def test_check_ranking_flush():
    hand = '2369Ts2h6d'
    assert calculate_hand_value_str(hand) == definitions.RANK_FLUSH


def test_check_ranking_full_house():
    hand = '236s2c23h9d'
    assert calculate_hand_value_str(hand) == definitions.RANK_FULL_HOUSE


def test_check_ranking_four_of_a_kind():
    hand = '236s2c2h29d'
    assert calculate_hand_value_str(hand) == definitions.RANK_FOUR_OF_A_KIND


def test_check_ranking_straight_flush():
    hand = '23456s7c9d'
    assert calculate_hand_value_str(hand) == definitions.RANK_STRAIGHT_FLUSH


def test_check_ranking_royal_flush():
    hand = 'TJQKAs7c9d'
    assert calculate_hand_value_str(hand) == definitions.RANK_ROYAL_FLUSH
