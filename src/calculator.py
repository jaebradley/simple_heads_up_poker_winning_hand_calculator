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

from collections import Counter
from model import Suit, Card, Hand
from hand_ranking_calculator import HandRankingCalculator


class HeadsUpWinnerSelector:

    def __init__(self):
        self.hand_ranking_calculator = HandRankingCalculator()

    def select_winning_hand(self, first_hand, second_hand):
        first_hand_ranking = self.hand_ranking_calculator.calculate_hand_ranking(first_hand)
        second_hand_ranking = self.hand_ranking_calculator.calculate_hand_ranking(second_hand)









