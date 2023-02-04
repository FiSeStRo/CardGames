from Backend import definitions

card_value_list = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King",
                   "Ace"]
card_color_list = ["Clubs", "Spades", "Hearts", "Diamonds"]


def get_card_name_idx(card_idx: int, show_card_idx=False):
    card_value = card_idx % definitions.NUM_CARDS_PER_COLOR
    card_color = card_idx // definitions.NUM_CARDS_PER_COLOR
    result_text = card_value_list[card_value] + " of " + card_color_list[card_color]
    if show_card_idx:
        result_text += " (" + str(card_idx) + ")"
    return result_text


def get_card_name_dict(card_dict: dict, show_card_idx=False):
    from Backend import converter
    converted_card = converter.convert_dict_to_idx(card_dict)
    return get_card_name_idx(converted_card, show_card_idx)
