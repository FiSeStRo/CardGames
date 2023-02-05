from Backend import definitions
from Backend import converter


def calculate_hand_value(card_list: dict):
    color_list = []
    value_list = []
    for card in card_list[definitions.DATA_CARDLIST]:
        color_list.append(card[definitions.DATA_CARD_COLOR])
        value_list.append(card[definitions.DATA_CARD_VALUE])

    color_list.sort()
    value_list.sort()

    if check_for_royal_flush(color_list, value_list):
        return definitions.RANK_ROYAL_FLUSH

    is_straight_flush, straight_highest_card = check_for_straight_flush(color_list, value_list)
    if is_straight_flush:
        return definitions.RANK_STRAIGHT_FLUSH

    is_foak, highest_card = check_for_four_of_a_kind(value_list)
    if is_foak:
        return definitions.RANK_FOUR_OF_A_KIND

    if check_for_full_house(value_list):
        return definitions.RANK_FULL_HOUSE

    is_flush, highest_card = check_for_flush(color_list)
    # TODO: highest flush not checkable with only the color list
    if is_flush:
        return definitions.RANK_FLUSH

    is_straight, straight_highest_card = check_for_straight(value_list)
    if is_straight:
        return definitions.RANK_STRAIGHT

    is_toak, highest_card = check_for_three_of_a_kind(value_list)
    if is_toak:
        return definitions.RANK_THREE_OF_A_KIND

    is_two_pair, pair_list = check_for_two_pair(value_list)
    if is_two_pair:
        return definitions.RANK_TWO_PAIR

    is_pair, pair_list = check_for_pair(value_list)
    if is_pair:
        return definitions.RANK_ONE_PAIR

    return definitions.RANK_HIGH_CARD


def calculate_hand_value_str(hand_string: str):
    hand_dict = converter.convert_hand_str_to_dict(hand_string)
    return calculate_hand_value(hand_dict)


def check_for_royal_flush(color_list: list, value_list: list):
    is_straight_flush, straight_highest_card = check_for_straight_flush(color_list, value_list)
    return is_straight_flush and straight_highest_card == definitions.CARD_ACE


def check_for_straight_flush(color_list: list, value_list: list):
    is_straight, straight_highest_card = check_for_straight(value_list)
    is_flush, flush_color = check_for_flush(color_list)
    return is_straight and is_flush, straight_highest_card


def check_for_four_of_a_kind(value_list: list):
    return check_for_amount_of_cards(value_list, 4, 1)


def check_for_full_house(value_list: list):
    is_toak, toak_card_value_list = check_for_three_of_a_kind(value_list)
    is_pair, pair_card_value_list = check_for_pair(value_list)
    # TODO: implementation
    # print(toak_card_value_list)
    # print(pair_card_value_list)

    # print(list(set(toak_card_value_list) ^ set(pair_card_value_list)))
    return False


def check_for_flush(color_list: list):
    return check_for_amount_of_cards(color_list, 5, 1)


def check_for_straight(value_list: list):
    unique_value_list = list(dict.fromkeys(value_list))
    if len(unique_value_list) < 5:
        return False

    straight_length = 0
    last_checked_value = -2
    for value in unique_value_list:
        if value == last_checked_value + 1:
            straight_length += 1
        elif straight_length >= 5:
            return True, last_checked_value
        else:
            straight_length = 1
        last_checked_value = value

    return straight_length >= 5, last_checked_value


def check_for_three_of_a_kind(value_list: list):
    return check_for_amount_of_cards(value_list, 3, 1)


def check_for_two_pair(value_list: list):
    return check_for_amount_of_cards(value_list, 2, 2)


def check_for_pair(value_list: list):
    return check_for_amount_of_cards(value_list, 2, 1)


def check_for_amount_of_cards(value_list: list, num_cards_required: int, num_occurence_required: int):
    value_dict = {i: value_list.count(i) for i in value_list}
    num_occurence_found = 0
    card_values_found = []
    for card_value, num_cards_found in value_dict.items():
        if num_cards_found >= num_cards_required:
            num_occurence_found += 1
            card_values_found.append(card_value)

    if len(card_values_found) > 1:
        card_values_found = card_values_found.reverse()
    return num_occurence_found >= num_occurence_required, card_values_found
