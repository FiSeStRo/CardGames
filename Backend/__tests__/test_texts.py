import pytest

from Backend import texts


def test_get_card_name_idx_without_card_idx():
    # test without showing card idx
    assert texts.get_card_name_idx(0) == "Two of Clubs"
    assert texts.get_card_name_idx(1) == "Three of Clubs"
    assert texts.get_card_name_idx(2) == "Four of Clubs"
    assert texts.get_card_name_idx(3) == "Five of Clubs"
    assert texts.get_card_name_idx(4) == "Six of Clubs"
    assert texts.get_card_name_idx(5) == "Seven of Clubs"
    assert texts.get_card_name_idx(6) == "Eight of Clubs"
    assert texts.get_card_name_idx(7) == "Nine of Clubs"
    assert texts.get_card_name_idx(8) == "Ten of Clubs"
    assert texts.get_card_name_idx(9) == "Jack of Clubs"
    assert texts.get_card_name_idx(10) == "Queen of Clubs"
    assert texts.get_card_name_idx(11) == "King of Clubs"
    assert texts.get_card_name_idx(12) == "Ace of Clubs"
    assert texts.get_card_name_idx(13) == "Two of Spades"
    assert texts.get_card_name_idx(14) == "Three of Spades"
    assert texts.get_card_name_idx(15) == "Four of Spades"
    assert texts.get_card_name_idx(16) == "Five of Spades"
    assert texts.get_card_name_idx(17) == "Six of Spades"
    assert texts.get_card_name_idx(18) == "Seven of Spades"
    assert texts.get_card_name_idx(19) == "Eight of Spades"
    assert texts.get_card_name_idx(20) == "Nine of Spades"
    assert texts.get_card_name_idx(21) == "Ten of Spades"
    assert texts.get_card_name_idx(22) == "Jack of Spades"
    assert texts.get_card_name_idx(23) == "Queen of Spades"
    assert texts.get_card_name_idx(24) == "King of Spades"
    assert texts.get_card_name_idx(25) == "Ace of Spades"
    assert texts.get_card_name_idx(26) == "Two of Hearts"
    assert texts.get_card_name_idx(27) == "Three of Hearts"
    assert texts.get_card_name_idx(28) == "Four of Hearts"
    assert texts.get_card_name_idx(29) == "Five of Hearts"
    assert texts.get_card_name_idx(30) == "Six of Hearts"
    assert texts.get_card_name_idx(31) == "Seven of Hearts"
    assert texts.get_card_name_idx(32) == "Eight of Hearts"
    assert texts.get_card_name_idx(33) == "Nine of Hearts"
    assert texts.get_card_name_idx(34) == "Ten of Hearts"
    assert texts.get_card_name_idx(35) == "Jack of Hearts"
    assert texts.get_card_name_idx(36) == "Queen of Hearts"
    assert texts.get_card_name_idx(37) == "King of Hearts"
    assert texts.get_card_name_idx(38) == "Ace of Hearts"
    assert texts.get_card_name_idx(39) == "Two of Diamonds"
    assert texts.get_card_name_idx(40) == "Three of Diamonds"
    assert texts.get_card_name_idx(41) == "Four of Diamonds"
    assert texts.get_card_name_idx(42) == "Five of Diamonds"
    assert texts.get_card_name_idx(43) == "Six of Diamonds"
    assert texts.get_card_name_idx(44) == "Seven of Diamonds"
    assert texts.get_card_name_idx(45) == "Eight of Diamonds"
    assert texts.get_card_name_idx(46) == "Nine of Diamonds"
    assert texts.get_card_name_idx(47) == "Ten of Diamonds"
    assert texts.get_card_name_idx(48) == "Jack of Diamonds"
    assert texts.get_card_name_idx(49) == "Queen of Diamonds"
    assert texts.get_card_name_idx(50) == "King of Diamonds"
    assert texts.get_card_name_idx(51) == "Ace of Diamonds"


def test_get_card_name_idx_with_card_idx():
    # test with showing card idx
    assert texts.get_card_name_idx(0, True) == "Two of Clubs (0)"
    assert texts.get_card_name_idx(1, True) == "Three of Clubs (1)"
    assert texts.get_card_name_idx(2, True) == "Four of Clubs (2)"
    assert texts.get_card_name_idx(3, True) == "Five of Clubs (3)"
    assert texts.get_card_name_idx(4, True) == "Six of Clubs (4)"
    assert texts.get_card_name_idx(5, True) == "Seven of Clubs (5)"
    assert texts.get_card_name_idx(6, True) == "Eight of Clubs (6)"
    assert texts.get_card_name_idx(7, True) == "Nine of Clubs (7)"
    assert texts.get_card_name_idx(8, True) == "Ten of Clubs (8)"
    assert texts.get_card_name_idx(9, True) == "Jack of Clubs (9)"
    assert texts.get_card_name_idx(10, True) == "Queen of Clubs (10)"
    assert texts.get_card_name_idx(11, True) == "King of Clubs (11)"
    assert texts.get_card_name_idx(12, True) == "Ace of Clubs (12)"
    assert texts.get_card_name_idx(13, True) == "Two of Spades (13)"
    assert texts.get_card_name_idx(14, True) == "Three of Spades (14)"
    assert texts.get_card_name_idx(15, True) == "Four of Spades (15)"
    assert texts.get_card_name_idx(16, True) == "Five of Spades (16)"
    assert texts.get_card_name_idx(17, True) == "Six of Spades (17)"
    assert texts.get_card_name_idx(18, True) == "Seven of Spades (18)"
    assert texts.get_card_name_idx(19, True) == "Eight of Spades (19)"
    assert texts.get_card_name_idx(20, True) == "Nine of Spades (20)"
    assert texts.get_card_name_idx(21, True) == "Ten of Spades (21)"
    assert texts.get_card_name_idx(22, True) == "Jack of Spades (22)"
    assert texts.get_card_name_idx(23, True) == "Queen of Spades (23)"
    assert texts.get_card_name_idx(24, True) == "King of Spades (24)"
    assert texts.get_card_name_idx(25, True) == "Ace of Spades (25)"
    assert texts.get_card_name_idx(26, True) == "Two of Hearts (26)"
    assert texts.get_card_name_idx(27, True) == "Three of Hearts (27)"
    assert texts.get_card_name_idx(28, True) == "Four of Hearts (28)"
    assert texts.get_card_name_idx(29, True) == "Five of Hearts (29)"
    assert texts.get_card_name_idx(30, True) == "Six of Hearts (30)"
    assert texts.get_card_name_idx(31, True) == "Seven of Hearts (31)"
    assert texts.get_card_name_idx(32, True) == "Eight of Hearts (32)"
    assert texts.get_card_name_idx(33, True) == "Nine of Hearts (33)"
    assert texts.get_card_name_idx(34, True) == "Ten of Hearts (34)"
    assert texts.get_card_name_idx(35, True) == "Jack of Hearts (35)"
    assert texts.get_card_name_idx(36, True) == "Queen of Hearts (36)"
    assert texts.get_card_name_idx(37, True) == "King of Hearts (37)"
    assert texts.get_card_name_idx(38, True) == "Ace of Hearts (38)"
    assert texts.get_card_name_idx(39, True) == "Two of Diamonds (39)"
    assert texts.get_card_name_idx(40, True) == "Three of Diamonds (40)"
    assert texts.get_card_name_idx(41, True) == "Four of Diamonds (41)"
    assert texts.get_card_name_idx(42, True) == "Five of Diamonds (42)"
    assert texts.get_card_name_idx(43, True) == "Six of Diamonds (43)"
    assert texts.get_card_name_idx(44, True) == "Seven of Diamonds (44)"
    assert texts.get_card_name_idx(45, True) == "Eight of Diamonds (45)"
    assert texts.get_card_name_idx(46, True) == "Nine of Diamonds (46)"
    assert texts.get_card_name_idx(47, True) == "Ten of Diamonds (47)"
    assert texts.get_card_name_idx(48, True) == "Jack of Diamonds (48)"
    assert texts.get_card_name_idx(49, True) == "Queen of Diamonds (49)"
    assert texts.get_card_name_idx(50, True) == "King of Diamonds (50)"
    assert texts.get_card_name_idx(51, True) == "Ace of Diamonds (51)"


# test with invalid card idx
def test_get_card_name_idx_with_invalid_card_idx():
    with pytest.raises(IndexError):
        assert texts.get_card_name_idx(52) == "Invalid card index"
