from Backend import definitions


def calculate_hand_value(card_list: dict):
    color_list = []
    value_list = []
    for card in card_list[definitions.DATA_CARDLIST]:
        color_list.append(card[definitions.DATA_CARD_COLOR])
        value_list.append(card[definitions.DATA_CARD_VALUE])

    color_list.sort()
    value_list.sort()

    if check_for_royal_flush(card_list):
        return definitions.RANK_ROYAL_FLUSH

    if check_for_straight_flush(card_list):
        return definitions.RANK_STRAIGHT_FLUSH

    if check_for_four_of_a_kind(value_list):
        return definitions.RANK_FOUR_OF_A_KIND

    if check_for_full_house(value_list):
        return definitions.RANK_FULL_HOUSE

    if check_for_flush(color_list):
        return definitions.RANK_FLUSH

    if check_for_straight(value_list):
        return definitions.RANK_STRAIGHT

    if check_for_three_of_a_kind(value_list):
        return definitions.RANK_THREE_OF_A_KIND

    if check_for_two_pair(value_list):
        return definitions.RANK_TWO_PAIR

    if check_for_pair(value_list):
        return definitions.RANK_ONE_PAIR

    return definitions.RANK_HIGH_CARD


def check_for_royal_flush(card_list: dict):
    return False


def check_for_straight_flush(card_list: dict):
    return False


def check_for_four_of_a_kind(value_list: list):
    return check_for_amount_of_cards(value_list, 4, 1)


def check_for_full_house(value_list: list):
    return False


def check_for_flush(color_list: list):
    return check_for_amount_of_cards(color_list, 5, 1)


def check_for_straight(value_list: list):
    return False


def check_for_three_of_a_kind(value_list: list):
    return check_for_amount_of_cards(value_list, 3, 1)


def check_for_two_pair(value_list: list):
    return check_for_amount_of_cards(value_list, 2, 2)


def check_for_pair(value_list: list):
    return check_for_amount_of_cards(value_list, 2, 1)


def check_for_amount_of_cards(value_list: list, num_cards_required: int, num_occurence_required: int):
    value_dict = {i: value_list.count(i) for i in value_list}
    num_occurence_found = 0
    for num_cards_found in value_dict.values():
        if num_cards_found >= num_cards_required:
            num_occurence_found += 1
    return num_occurence_found >= num_occurence_required
