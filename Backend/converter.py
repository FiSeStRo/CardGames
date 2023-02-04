from Backend import definitions
import re


def convert_idx_to_dict(card_idx: int):
    color = card_idx // definitions.NUM_CARDS_PER_COLOR
    value = card_idx % definitions.NUM_CARDS_PER_COLOR
    return {definitions.DATA_CARD_COLOR: color, definitions.DATA_CARD_VALUE: value}


# {c,v} -> 12
def convert_dict_to_idx(card_dict):
    return card_dict[definitions.DATA_CARD_COLOR] * definitions.NUM_CARDS_PER_COLOR + card_dict[
        definitions.DATA_CARD_VALUE]


# 'Ad' -> 51
def convert_str_to_idx(card_string):
    string_values = {
        'A': definitions.CARD_ACE,
        'K': definitions.CARD_KING,
        'Q': definitions.CARD_QUEEN,
        'J': definitions.CARD_JACK,
        'T': definitions.CARD_TEN,
        '9': definitions.CARD_NINE,
        '8': definitions.CARD_EIGHT,
        '7': definitions.CARD_SEVEN,
        '6': definitions.CARD_SIX,
        '5': definitions.CARD_FIVE,
        '4': definitions.CARD_FOUR,
        '3': definitions.CARD_THREE,
        '2': definitions.CARD_TWO,
        'c': definitions.COL_CLUB,
        's': definitions.COL_SPADE,
        'h': definitions.COL_HEART,
        'd': definitions.COL_DIAMOND,
    }
    card_value = string_values[card_string[0]]
    card_color = string_values[card_string[-1]]
    return card_color * definitions.NUM_CARDS_PER_COLOR + card_value


# [12, 13, 28, 7, 0] -> [{c,v},{c,v},{c,v},{c,v},{c,v}]
def convert_hand_idx_to_dict(card_idx_hand):
    card_dict_hand = {definitions.DATA_CARDLIST: []}
    for idx in card_idx_hand:
        card_dict_hand[definitions.DATA_CARDLIST].append(convert_idx_to_dict(idx))
    return card_dict_hand


# [12, 13, 28, 7, 0] -> [{c,v},{c,v},{c,v},{c,v},{c,v}]
def convert_hand_dict_to_idx(card_dict_hand):
    card_idx_hand = {definitions.DATA_CARDLIST: []}
    for dic in card_dict_hand:
        card_idx_hand[definitions.DATA_CARDLIST].append(convert_dict_to_idx(dic))
    return card_idx_hand


# 'QKAd' -> [49, 50, 51]
def convert_hand_str_to_idx(card_str_hand):
    idx_list = []
    result = list(filter(None, re.split(r'([AKQJT98765432]+[cshd])', card_str_hand)))
    for res in result:
        idx_list.extend(convert_str_group_to_idx(res))
    return idx_list


def convert_str_group_to_idx(str_group: str):
    idx_list = []
    card_color = str_group[-1]
    for card_value in str_group:
        if card_value != card_color:
            idx_list.append(convert_str_to_idx(card_value + card_color))
    return idx_list
