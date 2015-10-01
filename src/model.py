class Suit:
    Hearts, Diamonds, Spades, Clubs = range(4)


class Card:

    def __init__(self, high_value, low_value, suit):
        self.high_value = high_value
        self.low_value = low_value
        self.suit = suit

        assert 14 > self.high_value > 1
        assert 13 > self.low_value > 0

    def __str__(self):
        return "{0} - {1} - {2} ".format(self.high_value, self.low_value, self.suit)


class Hand:

    def __init__(self, cards):
        self.cards = cards

        assert cards.__len__() == 5
