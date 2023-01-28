from Backend import converter
from Backend import texts
from Backend import definitions

card_list = [23, 14, 27, 20, 5, 0, 2]
card_dict_list = converter.convert_hand_idx_to_dict(card_list)

for card_dict in card_dict_list[definitions.DATA_CARDLIST]:
    print(texts.get_card_name_dict(card_dict))
