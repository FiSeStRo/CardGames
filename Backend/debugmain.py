from Backend import ranking
from Backend import converter
from Backend import texts
from Backend import definitions

# string_hand = "AKQJTh3c5s"
string_hand = "2Js89c7Th5d"

print(texts.get_hand_name_string(string_hand))

hand_ranking = ranking.calculate_hand_value_str(string_hand)
print("==== Result ====")
print(texts.get_rank_name(hand_ranking))
