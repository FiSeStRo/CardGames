from Backend import definitions


def calculate_hand_value(card_list):
    color_list = []
    value_list = []
    for card in card_list:
        color_list.append(card["color"])
        value_list.append(card["value"])

    color_list.sort()
    value_list.sort()

    if check_for_royal_flush(card_list):
        return definitions.RANK_ROYAL_FLUSH

    if check_for_straight_flush(card_list):
        return definitions.RANK_STRAIGHT_FLUSH

    if check_for_four_of_a_kind(card_list):
        return definitions.RANK_FOUR_OF_A_KIND

    if check_for_full_house(card_list):
        return definitions.RANK_FULL_HOUSE

    if check_for_flush(card_list):
        return definitions.RANK_FLUSH

    if check_for_straight(card_list):
        return definitions.RANK_STRAIGHT

    if check_for_three_of_a_kind(card_list):
        return definitions.RANK_THREE_OF_A_KIND

    if check_for_two_pair(card_list):
        return definitions.RANK_TWO_PAIR

    if check_for_pair(card_list):
        return definitions.RANK_ONE_PAIR

    return definitions.RANK_HIGH_CARD


def check_for_royal_flush(card_list):
    return False


def check_for_straight_flush(card_list):
    return False


def check_for_four_of_a_kind(card_list):
    return False


def check_for_full_house(card_list):
    return False


def check_for_flush(card_list):
    return False


def check_for_straight(card_list):
    return False


def check_for_three_of_a_kind(card_list):
    return False


def check_for_two_pair(card_list):
    return False


def check_for_pair(card_list):
    return False
