import deck

print("Hello CardGames!")

shuffle_array = deck.create_shuffle_array()
print(shuffle_array)

for i in range(7):
    drawn_card = shuffle_array.pop(0)
    print(drawn_card)

print(shuffle_array)
