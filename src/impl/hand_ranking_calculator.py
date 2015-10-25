from src.interfaces.hand_ranking_calculator_interface import HandRankingCalculatorInterface
from src.model.hand_ranking import HighCard, OnePair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush
from src.impl.hand_ranking_verifier import HighCardVerifier, OnePairVerifier, TwoPairVerifier, ThreeOfAKindVerifier, StraightVerifier, FlushVerifier, FullHouseVerifier, FourOfAKindVerifier, StraightFlushVerifier
from collections import Counter
from src.model.card import Two, Three, Four, Five, Ace


class StraightFlushCalculator(HandRankingCalculatorInterface):

    @staticmethod
    def calculate_hand_ranking(hand):
        if StraightFlushVerifier.verify_hand_ranking(hand):
            # Check for low straight case
            if any(isinstance(card, Ace) for card in hand.cards) and any(isinstance(card, Two) for card in hand.cards) and any(isinstance(card, Three) for card in hand.cards) and any(isinstance(card, Four) for card in hand.cards) and any(isinstance(card, Five) for card in hand.cards):
                high_card = [card for card in hand.cards if isinstance(card, Five)][0]
                return StraightFlush(high_card)
            high_card_value = 0
            high_card = None
            for card in hand.cards:
                if card.value > high_card_value:
                    high_card = card
                    high_card_value = card.value
            return StraightFlush(high_card)
        else:
            raise RuntimeError("hand is not straight flush")

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)


class FourOfAKindCalculator(HandRankingCalculatorInterface):

    @staticmethod
    def calculate_hand_ranking(hand):
        if FourOfAKindVerifier.verify_hand_ranking(hand):
            card_values = [card.value for card in hand.cards]
            card_counter = Counter(card_values)
            if 4 == card_counter[card_values[0]]:
                four_of_a_kind_value = card_values[0]
                kicker = [card.value for card in hand.cards if card.value != four_of_a_kind_value][0]
            else:
                four_of_a_kind_value = card_values[1]
                kicker = card_values[0]
            return FourOfAKind(four_of_a_kind_value, kicker)
        else:
            raise RuntimeError("hand is not four of a kind")

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)


class FullHouseCalculator(HandRankingCalculatorInterface):

    @staticmethod
    def calculate_hand_ranking(hand):
        if FullHouseVerifier.verify_hand_ranking(hand):
            card_values = [card.value for card in hand.cards]
            card_counter = Counter(card_values)
            if 3 == card_counter[card_values[0]]:
                three_of_a_kind_value = card_values[0]
                two_of_a_kind_value = [card.value for card in hand.cards if card.value != three_of_a_kind_value][0]
            else:
                two_of_a_kind_value = card_values[0]
                three_of_a_kind_value = [card.value for card in hand.cards if card.value != two_of_a_kind_value][0]
            return FullHouse(three_of_a_kind_value, two_of_a_kind_value)
        else:
            raise RuntimeError("hand is not full house")

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)


class StraightCalculator(HandRankingCalculatorInterface):

    @staticmethod
    def calculate_hand_ranking(hand):
        if StraightVerifier.verify_hand_ranking(hand) and not StraightFlushVerifier.verify_hand_ranking(hand):
            # Check for low straight case
            if any(isinstance(card, Ace) for card in hand.cards) and any(isinstance(card, Two) for card in hand.cards) and any(isinstance(card, Three) for card in hand.cards) and any(isinstance(card, Four) for card in hand.cards) and any(isinstance(card, Five) for card in hand.cards):
                high_value = [card for card in hand.cards if isinstance(card, Five)][0].value
                return Straight(high_value)
            high_value = sorted([card.value for card in hand.cards], reverse=True)[0]
            return Straight(high_value)
        else:
            raise RuntimeError("hand is not straight")

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)


class FlushCalculator(HandRankingCalculatorInterface):

    @staticmethod
    def calculate_hand_ranking(hand):
        if FlushVerifier.verify_hand_ranking(hand) and not StraightFlushVerifier.verify_hand_ranking(hand):
            suit = hand.cards[0].suit
            sorted_card_values = sorted([card.value for card in hand.cards], reverse=True)
            return Flush(
                suit,
                first_kicker=sorted_card_values[0],
                second_kicker=sorted_card_values[1],
                third_kicker=sorted_card_values[2],
                fourth_kicker=sorted_card_values[3],
                fifth_kicker=sorted_card_values[4]
            )
        else:
            raise RuntimeError("hand is not flush")

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)


class ThreeOfAKindCalculator(HandRankingCalculatorInterface):

    @staticmethod
    def calculate_hand_ranking(hand):
        if ThreeOfAKindVerifier.verify_hand_ranking(hand):
            three_of_a_kind_value = max(set(hand.cards), key=hand.cards.count).value
            sorted_card_values = sorted([card.value for card in hand.cards if card.value != three_of_a_kind_value], reverse=True)
            first_kicker_value = sorted_card_values[0]
            second_kicker_value = sorted_card_values[1]
            return ThreeOfAKind(
                three_of_a_kind_value,
                first_kicker_value,
                second_kicker_value
            )
        else:
            raise RuntimeError("hand is not three of a kind")

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)


class TwoPairCalculator(HandRankingCalculatorInterface):

    @staticmethod
    def calculate_hand_ranking(hand):
        if TwoPairVerifier.verify_hand_ranking(hand):
            hand_value_counter = Counter([card.value for card in hand.cards])
            hand_most_common_values = hand_value_counter.most_common()
            hand_highest_pair_value = max(hand_most_common_values[0][0], hand_most_common_values[1][0])
            hand_lowest_pair_value = min(hand_most_common_values[0][0], hand_most_common_values[1][0])
            hand_kicker_value = hand_most_common_values[2][0]
            return TwoPair(
                hand_highest_pair_value,
                hand_lowest_pair_value,
                hand_kicker_value
            )
        else:
            raise RuntimeError("hand is not two pair")

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)


class OnePairCalculator(HandRankingCalculatorInterface):

    @staticmethod
    def calculate_hand_ranking(hand):
        if OnePairVerifier.verify_hand_ranking(hand):
            hand_value_counter = Counter([card.value for card in hand.cards])
            hand_most_common_values = hand_value_counter.most_common()
            pair_value = hand_most_common_values[0][0]
            sorted_values = sorted([card.value for card in hand.cards if card.value != pair_value], reverse=True)
            return OnePair(
                pair_value,
                sorted_values[0],
                sorted_values[1],
                sorted_values[2]
            )
        else:
            raise RuntimeError("hand is not one pair")

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)


class HighCardCalculator(HandRankingCalculatorInterface):

    @staticmethod
    def calculate_hand_ranking(hand):
        if HighCardVerifier.verify_hand_ranking(hand):
            sorted_card_values = sorted([card.value for card in hand.cards], reverse=True)
            return HighCard(
                sorted_card_values[0],
                sorted_card_values[1],
                sorted_card_values[2],
                sorted_card_values[3],
                sorted_card_values[4]
            )
        else:
            raise RuntimeError("hand is not high card")

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)


class HandRankingCalculator(HandRankingCalculatorInterface):

    def __init__(self):
        HandRankingCalculatorInterface.__init__(self)

    @staticmethod
    def calculate_hand_ranking(hand):
        if StraightFlushVerifier.verify_hand_ranking(hand):
            return StraightFlushCalculator.calculate_hand_ranking(hand)
        else:
            if FourOfAKindVerifier.verify_hand_ranking(hand):
                return FourOfAKindCalculator.calculate_hand_ranking(hand)
            else:
                if FullHouseVerifier.verify_hand_ranking(hand):
                    return FullHouseCalculator.calculate_hand_ranking(hand)
                else:
                    if FlushVerifier.verify_hand_ranking(hand):
                        return FlushCalculator.calculate_hand_ranking(hand)
                    else:
                        if StraightVerifier.verify_hand_ranking(hand):
                            return StraightCalculator.calculate_hand_ranking(hand)
                        else:
                            if ThreeOfAKindVerifier.verify_hand_ranking(hand):
                                return ThreeOfAKindCalculator.calculate_hand_ranking(hand)
                            else:
                                if TwoPairVerifier.verify_hand_ranking(hand):
                                    return TwoPairCalculator.calculate_hand_ranking(hand)
                                else:
                                    if OnePairVerifier.verify_hand_ranking(hand):
                                        return OnePairCalculator.calculate_hand_ranking(hand)
                                    else:
                                        if HighCardVerifier.verify_hand_ranking(hand):
                                            return HighCardCalculator.calculate_hand_ranking(hand)
                                        else:
                                            raise RuntimeError("unknown hand ranking")