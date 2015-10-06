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
                heads_up_winner = HeadsUpResult.FirstHand
            elif first_hand_ranking.high_value < second_hand_ranking.high_value:
                heads_up_winner = HeadsUpResult.SecondHand
            else:
                heads_up_winner = HeadsUpResult.Tie
            return heads_up_winner
        else:
            raise RuntimeError("unexpected hand ranking")

    @staticmethod
    def calculate_result_for_two_four_of_a_kinds(first_hand_ranking, second_hand_ranking):
        if isinstance(first_hand_ranking, FourOfAKind) and isinstance(second_hand_ranking, FourOfAKind):
            if first_hand_ranking.four_of_a_kind_value > second_hand_ranking.four_of_a_kind_value:
                heads_up_winner = HeadsUpResult.FirstHand
            elif first_hand_ranking.four_of_a_kind_value < second_hand_ranking.four_of_a_kind_value:
                heads_up_winner = HeadsUpResult.SecondHand
            else:
                if first_hand_ranking.kicker_value > second_hand_ranking.kicker_value:
                    heads_up_winner = HeadsUpResult.FirstHand
                elif first_hand_ranking.kicker_value < second_hand_ranking.kicker_value:
                    heads_up_winner = HeadsUpResult.SecondHand
                else:
                    heads_up_winner = HeadsUpResult.Tie
            return heads_up_winner
        else:
            raise RuntimeError("unexpected hand ranking")

    @staticmethod
    def calculate_result_for_two_full_houses(first_hand_ranking, second_hand_ranking):
        


class HeadsUpResultCalculator:

    def __init__(self):
        self.hand_ranking_calculator = HandRankingCalculator()

    def calculate_result(self, first_hand, second_hand):
        first_hand_ranking = self.hand_ranking_calculator.calculate_hand_ranking(first_hand)
        second_hand_ranking = self.hand_ranking_calculator.calculate_hand_ranking(second_hand)
        if first_hand_ranking.value > second_hand_ranking.value:
            heads_up_winner = HeadsUpResult.FirstHand
        elif first_hand_ranking.value < second_hand_ranking.value:
            heads_up_winner = HeadsUpResult.SecondHand
        else:
            if type(first_hand_ranking) == type(second_hand_ranking):
                if isinstance(first_hand_ranking, StraightFlush):
                    if first_hand_ranking.high_value > second_hand_ranking.high_value:
                        heads_up_winner = HeadsUpResult.FirstHand
                    elif first_hand_ranking.high_value < second_hand_ranking.high_value:
                        heads_up_winner = HeadsUpResult.SecondHand
                    else:
                        heads_up_winner = HeadsUpResult.Tie
                elif isinstance(first_hand, FourOfAKind):
                    if first_hand_ranking.four_of_a_kind_value > second_hand_ranking.four_of_a_kind_value:
                        heads_up_winner = HeadsUpResult.FirstHand
                    elif first_hand_ranking.four_of_a_kind_value < second_hand_ranking.four_of_a_kind_value:
                        heads_up_winner = HeadsUpResult.SecondHand
                    else:
                        if
                        heads_up_winner = HeadsUpResult.Tie









