"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
"""

from model import HighCard, OnePair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush
from hand_ranking_calculator import HandRankingCalculator


class HeadsUpResult:
    FirstHand, SecondHand, Tie = range(3)


class IdenticalHandRankingHeadsUpResultCalculator:

    def __init__(self):
        pass

    @staticmethod
    def calculate_result_for_two_straight_flushes(first_hand_ranking, second_hand_ranking):
        if isinstance(first_hand_ranking, StraightFlush) and isinstance(second_hand_ranking, StraightFlush):
            if first_hand_ranking.high_value > second_hand_ranking.high_value:
                result = HeadsUpResult.FirstHand
            elif first_hand_ranking.high_value < second_hand_ranking.high_value:
                result = HeadsUpResult.SecondHand
            else:
                result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    @staticmethod
    def calculate_result_for_two_four_of_a_kinds(first_hand_ranking, second_hand_ranking):
        if isinstance(first_hand_ranking, FourOfAKind) and isinstance(second_hand_ranking, FourOfAKind):
            if first_hand_ranking.four_of_a_kind_value > second_hand_ranking.four_of_a_kind_value:
                result = HeadsUpResult.FirstHand
            elif first_hand_ranking.four_of_a_kind_value < second_hand_ranking.four_of_a_kind_value:
                result = HeadsUpResult.SecondHand
            else:
                if first_hand_ranking.kicker_value > second_hand_ranking.kicker_value:
                    result = HeadsUpResult.FirstHand
                elif first_hand_ranking.kicker_value < second_hand_ranking.kicker_value:
                    result = HeadsUpResult.SecondHand
                else:
                    result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    @staticmethod
    def calculate_result_for_two_full_houses(first_hand_ranking, second_hand_ranking):
        if isinstance(first_hand_ranking, FullHouse) and isinstance(second_hand_ranking, FullHouse):
            if first_hand_ranking.three_of_a_kind_value > second_hand_ranking.three_of_a_kind_value:
                result = HeadsUpResult.FirstHand
            elif first_hand_ranking.three_of_a_kind_value < second_hand_ranking.three_of_a_kind_value:
                result = HeadsUpResult.SecondHand
            else:
                if first_hand_ranking.two_of_a_kind_value > second_hand_ranking.two_of_a_kind_value:
                    result = HeadsUpResult.FirstHand
                elif first_hand_ranking.two_of_a_kind_value < second_hand_ranking.two_of_a_kind_value:
                    result = HeadsUpResult.SecondHand
                else:
                    result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    @staticmethod
    def calculate_result_for_flushes(first_hand_ranking, second_hand_ranking):
        if isinstance(first_hand_ranking, Flush) and isinstance(second_hand_ranking, Flush):
            if first_hand_ranking.first_kicker > second_hand_ranking.first_kicker:
                result = HeadsUpResult.FirstHand
            elif first_hand_ranking.first_kicker < second_hand_ranking.first_kicker:
                result = HeadsUpResult.SecondHand
            else:
                if first_hand_ranking.second_kicker > second_hand_ranking.second_kicker:
                    result = HeadsUpResult.FirstHand
                elif first_hand_ranking.second_kicker < second_hand_ranking.second_kicker:
                    result = HeadsUpResult.SecondHand
                else:
                    if first_hand_ranking.third_kicker > second_hand_ranking.third_kicker:
                        result = HeadsUpResult.FirstHand
                    elif first_hand_ranking.third_kicker < second_hand_ranking.third_kicker:
                        result = HeadsUpResult.SecondHand
                    else:
                        if first_hand_ranking.fourth_kicker > second_hand_ranking.fourth_kicker:
                            result = HeadsUpResult.FirstHand
                        elif first_hand_ranking.fourth_kicker < second_hand_ranking.fourth_kicker:
                            result = HeadsUpResult.SecondHand
                        else:
                            if first_hand_ranking.fifth_kicker > second_hand_ranking.fifth_kicker:
                                result = HeadsUpResult.FirstHand
                            elif first_hand_ranking < second_hand_ranking.fifth_kicker:
                                result = HeadsUpResult.SecondHand
                            else:
                                result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    @staticmethod
    def calculate_result_for_straights(first_hand_ranking, second_hand_ranking):
        if isinstance(first_hand_ranking, Straight) and isinstance(second_hand_ranking, Straight):
            if first_hand_ranking.high_value > second_hand_ranking.high_value:
                result = HeadsUpResult.FirstHand
            elif first_hand_ranking.high_value < second_hand_ranking.high_value:
                result = HeadsUpResult.SecondHand
            else:
                result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")




class HeadsUpResultCalculator:

    def __init__(self):
        self.hand_ranking_calculator = HandRankingCalculator()
        self.identical_hand_ranking_result_calcaultor = IdenticalHandRankingHeadsUpResultCalculator()

    def calculate_result(self, first_hand, second_hand):
        first_hand_ranking = self.hand_ranking_calculator.calculate_hand_ranking(first_hand)
        second_hand_ranking = self.hand_ranking_calculator.calculate_hand_ranking(second_hand)
        if first_hand_ranking.value > second_hand_ranking.value:
            result = HeadsUpResult.FirstHand
        elif first_hand_ranking.value < second_hand_ranking.value:
            result = HeadsUpResult.SecondHand
        else:
            if type(first_hand_ranking) == type(second_hand_ranking):
                if isinstance(first_hand_ranking, StraightFlush):
                    result = self.identical_hand_ranking_result_calcaultor.calculate_result_for_two_straight_flushes(
                        first_hand_ranking, second_hand_ranking
                    )
                elif isinstance(first_hand_ranking, FourOfAKind):
                    result = self.identical_hand_ranking_result_calcaultor.calculate_result_for_two_four_of_a_kinds(
                        first_hand_ranking, second_hand_ranking
                    )
                elif isinstance(first_hand_ranking, FullHouse):










