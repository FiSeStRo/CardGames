from Backend import definitions


def convert_idx_to_dict(card_idx: int):
    color = card_idx // definitions.NUM_CARDS_PER_COLOR
    value = card_idx % definitions.NUM_CARDS_PER_COLOR
    return {definitions.DATA_CARD_COLOR: color, definitions.DATA_CARD_VALUE: value}


# {c,v} -> 12
def convert_dict_to_idx(card_dict):
    return card_dict[definitions.DATA_CARD_COLOR] * definitions.NUM_CARDS_PER_COLOR + card_dict[definitions.DATA_CARD_VALUE]


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
