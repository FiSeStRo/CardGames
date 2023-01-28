from Backend import deck
from Backend import texts

print("Hello CardGames!")

shuffle_array = deck.create_deck()
print(shuffle_array)

for i in range(7):
    drawn_card = shuffle_array.pop(0)
    print(texts.get_card_name(drawn_card))

