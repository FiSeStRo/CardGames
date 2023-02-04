from Backend import ranking
from Backend import converter
from Backend import texts
from Backend import definitions

card_list = [23, 14, 27, 20, 5, 0, 2]
card_dict_list = converter.convert_hand_idx_to_dict(card_list)

for card_idx in card_list:
    print(texts.get_card_name_idx(card_idx))

hand_ranking = ranking.calculate_hand_value(card_dict_list)
print("==== Result ====")
print(texts.get_rank_name(hand_ranking))
