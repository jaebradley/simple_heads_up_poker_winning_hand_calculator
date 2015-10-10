class HandRanking:
    def __init__(self, rank_value):
        self.rank_value = rank_value


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
