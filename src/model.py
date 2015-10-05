class Suit:
    Hearts, Diamonds, Spades, Clubs = range(4)


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        assert 14 > self.value > 1

    def __str__(self):
        return "{0} - {1}".format(self.value, self.suit)


class Two(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 2, suit)


class Three(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 3, suit)


class Four(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 4, suit)


class Five(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 5, suit)


class Six(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 6, suit)


class Seven(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 7, suit)


class Eight(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 8, suit)


class Nine(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 9, suit)


class Ten(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 10, suit)


class Jack(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 11, suit)


class Queen(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 12, suit)


class King(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 13, suit)


class Ace(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 14, suit)


class Hand:

    def __init__(self, cards):
        self.cards = cards

        assert isinstance(cards, list)
        assert [isinstance(card, Card) for card in cards]

        assert cards.__len__() == 5


class HandRanking:
    def __init__(self, rank):
        self.rank = rank


class StraightFlush(HandRanking):

    def __init__(self, high_card):
        HandRanking.__init__(self, 9)
        self.high_value = high_card.value
        self.suit = high_card.suit


class FourOfAKind(HandRanking):
    def __init__(self, four_of_a_kind_value, kicker_value):
        HandRanking.__init__(self, 8)
        self.four_of_a_kind_value = four_of_a_kind_value
        self.kicker_value = kicker_value


class FullHouse(HandRanking):
    def __init__(self, three_of_a_kind_value, two_of_a_kind_value):
        HandRanking.__init__(self, 7)
        self.three_of_a_kind_value = three_of_a_kind_value
        self.two_of_a_kind_value = two_of_a_kind_value


class Flush(HandRanking):
    def __init__(self, suit, first_kicker, second_kicker, third_kicker, fourth_kicker, fifth_kicker):
        HandRanking.__init__(self, 6)
        self.suit = suit
        self.first_kicker = first_kicker
        self.second_kicker = second_kicker
        self.third_kicker = third_kicker
        self.fourth_kicker = fourth_kicker
        self.fifth_kicker = fifth_kicker


class Straight(HandRanking):

    def __init__(self, high_value):
        HandRanking.__init__(self, 1)
        self.high_value = high_value


class ThreeOfAKind(HandRanking):
    def __init__(self, three_of_a_kind_value, first_kicker_value, second_kicker_value):
        HandRanking.__init__(self, 1)
        self.three_of_a_kind_value = three_of_a_kind_value
        self.first_kicker_value = first_kicker_value
        self.second_kicker_value = second_kicker_value


class TwoPair(HandRanking):
    def __init__(self, highest_pair_value, lowest_pair_value, kicker_value):
        HandRanking.__init__(self, 1)
        self.highest_pair_value = highest_pair_value
        self.lowest_pair_value = lowest_pair_value
        self.kicker_value = kicker_value


class OnePair(HandRanking):
    def __init__(self, pair_value, first_kicker_value, second_kicker_value, third_kicker_value):
        HandRanking.__init__(self, 1)
        self.pair_value = pair_value
        self.first_kicker_value = first_kicker_value
        self.second_kicker_value = second_kicker_value
        self.third_kicker_value = third_kicker_value


class HighCard(HandRanking):
    def __init__(self, high_card_value, first_kicker_value, second_kicker_value, third_kicker_value, fourth_kicker_value):
        HandRanking.__init__(self, 1)
        self.high_card_value = high_card_value
        self.first_kicker_value = first_kicker_value
        self.second_kicker_value = second_kicker_value
        self.third_kicker_value = third_kicker_value
        self.fourth_kicker_value = fourth_kicker_value