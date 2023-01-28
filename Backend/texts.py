from Backend import definitions

card_value_list = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King",
                   "Ace"]
card_color_list = ["Clubs", "Spades", "Hearts", "Diamonds"]

ranking_list = {
        definitions.RANK_HIGH_CARD: "High Card",
        definitions.RANK_ONE_PAIR: "One Pair",
        definitions.RANK_TWO_PAIR: "Two Pairs",
        definitions.RANK_THREE_OF_A_KIND: "Three of a kind",
        definitions.RANK_STRAIGHT: "Straight",
        definitions.RANK_FLUSH: "Flush",
        definitions.RANK_FULL_HOUSE: "Full House",
        definitions.RANK_FOUR_OF_A_KIND: "Four of a kind",
        definitions.RANK_STRAIGHT_FLUSH: "Straight Flush",
        definitions.RANK_ROYAL_FLUSH: "Royal Flush",
    }


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


def get_rank_name(rank: int):
    return ranking_list[rank]
