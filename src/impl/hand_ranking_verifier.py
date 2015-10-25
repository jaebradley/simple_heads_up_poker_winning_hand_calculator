from collections import Counter
from src.interfaces.hand_ranking_verifier_interface import HandRankingVerifierInterface
from src.model.card import Two, Three, Four, Five, Ace


class FlushVerifier(HandRankingVerifierInterface):

    @staticmethod
    def verify_hand_ranking(hand):
        if 1 == len(set([card.suit for card in hand.cards])):
            return True
        else:
            return False

    def __init__(self):
        HandRankingVerifierInterface.__init__(self)


class StraightVerifier(HandRankingVerifierInterface):

    @staticmethod
    def verify_hand_ranking(hand):
        sorted_cards_by_greatest_values = sorted([card.value for card in hand.cards], reverse=True)
        is_straight_boolean = True
        for card_index in range(0, 4):
            if sorted_cards_by_greatest_values[card_index] - 1 != sorted_cards_by_greatest_values[card_index + 1]:
                is_straight_boolean = False
                break
        #  hard-coded check for ace case
        if any(isinstance(card, Ace) for card in hand.cards) and any(isinstance(card, Two) for card in hand.cards) and any(isinstance(card, Three) for card in hand.cards) and any(isinstance(card, Four) for card in hand.cards) and any(isinstance(card, Five) for card in hand.cards):
            is_straight_boolean = True
        return is_straight_boolean

    def __init__(self):
        HandRankingVerifierInterface.__init__(self)


class StraightFlushVerifier(HandRankingVerifierInterface):

    @staticmethod
    def verify_hand_ranking(hand):
        if FlushVerifier.verify_hand_ranking(hand) and StraightVerifier.verify_hand_ranking(hand):
            return True
        else:
            return False

    def __init__(self):
        HandRankingVerifierInterface.__init__(self)


class FourOfAKindVerifier(HandRankingVerifierInterface):

    @staticmethod
    def verify_hand_ranking(hand):
        card_values = [card.value for card in hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 2 and (card_counter[card_values[0]] == 4 or card_counter[card_values[0]] == 1):
            return True
        else:
            return False

    def __init__(self):
        HandRankingVerifierInterface.__init__(self)


class FullHouseVerifier(HandRankingVerifierInterface):

    @staticmethod
    def verify_hand_ranking(hand):
        card_values = [card.value for card in hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 2 and (card_counter[card_values[0]] == 3 or card_counter[card_values[0]] == 2):
            return True
        else:
            return False

    def __init__(self):
        HandRankingVerifierInterface.__init__(self)


class ThreeOfAKindVerifier(HandRankingVerifierInterface):

    @staticmethod
    def verify_hand_ranking(hand):
        card_values = [card.value for card in hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 3 and (card_counter[card_values[0]] == 3 or card_counter[card_values[1]] == 3 or card_counter[card_values[2]] == 3):
            return True
        else:
            return False

    def __init__(self):
        HandRankingVerifierInterface.__init__(self)


class TwoPairVerifier(HandRankingVerifierInterface):

    @staticmethod
    def verify_hand_ranking(hand):
        card_values = [card.value for card in hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 3 and (card_counter[card_values[0]] == 2 or card_counter[card_values[1]] == 2 or card_counter[card_values[2]] == 2):
            return True
        else:
            return False

    def __init__(self):
        HandRankingVerifierInterface.__init__(self)


class OnePairVerifier(HandRankingVerifierInterface):

    @staticmethod
    def verify_hand_ranking(hand):
        distinct_card_values = list(set([card.value for card in hand.cards]))
        if distinct_card_values.__len__() == 4:
            return True
        else:
            return False

    def __init__(self):
        HandRankingVerifierInterface.__init__(self)


class HighCardVerifier(HandRankingVerifierInterface):

    @staticmethod
    def verify_hand_ranking(hand):
        distinct_card_values = list(set([card.value for card in hand.cards]))
        if not StraightVerifier.verify_hand_ranking(hand) and not FlushVerifier.verify_hand_ranking(hand) and distinct_card_values.__len__() == 5:
            return True
        else:
            return False

    def __init__(self):
        HandRankingVerifierInterface.__init__(self)