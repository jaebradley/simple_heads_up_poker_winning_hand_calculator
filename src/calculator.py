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

    def __init__(self, handA, handB):
        self.handA_ranking_calculator = HandRankingCalculator(handA)
        self.handB_ranking_calculator = HandRankingCalculator(handB)

    def select_winning_hand(self):
        if self.handA_ranking_calculator.is_straight_flush() and not self.handB_ranking_calculator.is_straight_flush():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_straight_flush() and self.handB_ranking_calculator.is_straight_flush():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_straight_flush() and self.handB_ranking_calculator.is_straight_flush():
            handA_highest_card_value = sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True)[0]
            handB_highest_card_value = sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards], reverse=True)[0]
            if handA_highest_card_value > handB_highest_card_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_highest_card_value < handB_highest_card_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                winning_hand = None

        elif self.handA_ranking_calculator.is_four_of_a_kind() and not self.handB_ranking_calculator.is_four_of_a_kind():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_four_of_a_kind() and self.handB_ranking_calculator.is_four_of_a_kind():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_four_of_a_kind() and self.handB_ranking_calculator.is_four_of_a_kind():
            handA_four_of_a_kind_value = max(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
            handB_four_of_a_kind_value = max(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
            if handA_four_of_a_kind_value > handB_four_of_a_kind_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_four_of_a_kind_value < handB_four_of_a_kind_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                handA_kicker = min(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
                handB_kicker = min(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
                if handA_kicker > handB_kicker:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_kicker < handB_kicker:
                    winning_hand = self.handB_ranking_calculator.hand
                else:
                    winning_hand = None
        elif self.handA_ranking_calculator.is_full_house() and not self.handB_ranking_calculator.is_full_house():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_full_house() and self.handB_ranking_calculator.is_full_house():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_full_house() and self.handB_ranking_calculator.is_full_house():
            handA_three_of_a_kind_value = max(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
            handB_three_of_a_kind_value = max(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
            if handA_three_of_a_kind_value > handB_three_of_a_kind_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_three_of_a_kind_value < handB_three_of_a_kind_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                handA_two_of_a_kind_value = min(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
                handB_two_of_a_kind_value = min(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
                if handA_two_of_a_kind_value > handB_two_of_a_kind_value:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_two_of_a_kind_value < handB_two_of_a_kind_value:
                    winning_hand = self.handB_ranking_calculator.hand
                else:
                    winning_hand = None
        elif self.handA_ranking_calculator.is_flush() and not self.handB_ranking_calculator.is_flush():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_flush() and self.handB_ranking_calculator.is_flush():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_flush() and self.handB_ranking_calculator.is_flush():
            sorted_handA = list(sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True))
            sorted_handB = list(sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True))
            winning_hand = None
            for card_index in range(0, 5):
                if sorted_handA[card_index] > sorted_handB[card_index]:
                    winning_hand = self.handA_ranking_calculator.hand
                    break
                elif sorted_handA[card_index] < sorted_handB[card_index]:
                    winning_hand = self.handB_ranking_calculator.hand
                    break
        elif self.handA_ranking_calculator.is_straight() and not self.handB_ranking_calculator.is_straight():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_straight() and self.handB_ranking_calculator.is_straight():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_straight() and self.handB_ranking_calculator.is_straight():
            handA_highest_card_value = sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True)[0]
            handB_highest_card_value = sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards], reverse=True)[0]
            if handA_highest_card_value > handB_highest_card_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_highest_card_value < handB_highest_card_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                winning_hand = None
        elif self.handA_ranking_calculator.is_three_of_a_kind() and not self.handB_ranking_calculator.is_three_of_a_kind():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_three_of_a_kind() and self.handB_ranking_calculator.is_three_of_a_kind():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_three_of_a_kind() and self.handB_ranking_calculator.is_three_of_a_kind():
            handA_three_of_a_kind_value = max(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
            handB_three_of_a_kind_value = max(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
            if handA_three_of_a_kind_value > handB_three_of_a_kind_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_three_of_a_kind_value < handB_three_of_a_kind_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                handA_sorted_remaining_values = sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards if card.high_value != handA_three_of_a_kind_value], reverse=True)
                handB_sorted_remaining_values = sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards if card.high_value != handB_three_of_a_kind_value], reverse=True)
                if handA_sorted_remaining_values[0] > handB_sorted_remaining_values[0]:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_sorted_remaining_values[0] < handB_sorted_remaining_values[0]:
                    winning_hand = self.handB_ranking_calculator.hand
                elif handA_sorted_remaining_values[1] > handB_sorted_remaining_values[1]:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_sorted_remaining_values[0] < handB_sorted_remaining_values[1]:
                    winning_hand = self.handB_ranking_calculator.hand
                else:
                    winning_hand = None
        elif self.handA_ranking_calculator.is_two_pair() and not self.handB_ranking_calculator.is_two_pair():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_two_pair() and self.handB_ranking_calculator.is_two_pair():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_two_pair() and self.handB_ranking_calculator.is_two_pair():
            handA_value_counter = Counter([card.high_value for card in self.handA_ranking_calculator.hand.cards])
            handB_value_counter = Counter([card.high_value for card in self.handB_ranking_calculator.hand.cards])
            handA_most_common_values = handA_value_counter.most_common()
            handB_most_common_values = handB_value_counter.most_common()
            handA_highest_pair_value = max(handA_most_common_values[0][0], handA_most_common_values[1][0])
            handA_lowest_pair_value = min(handA_most_common_values[0][0], handA_most_common_values[1][0])
            handA_kicker_value = handA_most_common_values[2][0]
            handB_highest_pair_value = max(handB_most_common_values[0][0], handB_most_common_values[1][0])
            handB_lowest_pair_value = min(handB_most_common_values[0][0], handB_most_common_values[1][0])
            handB_kicker_value = handB_most_common_values[2][0]
            if handA_highest_pair_value > handB_highest_pair_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_highest_pair_value < handB_highest_pair_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                if handA_lowest_pair_value > handB_lowest_pair_value:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_lowest_pair_value < handB_lowest_pair_value:
                    winning_hand = self.handB_ranking_calculator.hand
                else:
                    if handA_kicker_value > handB_kicker_value:
                        winning_hand = self.handA_ranking_calculator.hand
                    elif handA_kicker_value < handB_kicker_value:
                        winning_hand = self.handB_ranking_calculator.hand
                    else:
                        winning_hand = None
        elif self.handA_ranking_calculator.is_one_pair() and not self.handB_ranking_calculator.is_one_pair():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_one_pair() and self.handB_ranking_calculator.is_one_pair():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_one_pair() and self.handB_ranking_calculator.is_one_pair():
            handA_value_counter = Counter([card.high_value for card in self.handA_ranking_calculator.hand.cards])
            handB_value_counter = Counter([card.high_value for card in self.handB_ranking_calculator.hand.cards])
            handA_most_common_value = handA_value_counter.most_common(1)[0][0]
            handB_most_common_value = handB_value_counter.most_common(1)[0][0]
            if handA_most_common_value > handB_most_common_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_most_common_value < handB_most_common_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                handA_sorted_remaining_values = list(sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards if card.high_value != handA_most_common_value], reverse=True))
                handB_sorted_remaining_values = list(sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards if card.high_value != handB_most_common_value], reverse=True))
                winning_hand = None
                for card_index in range(0, 3):
                    if handA_sorted_remaining_values[card_index] > handB_sorted_remaining_values[card_index]:
                        winning_hand = self.handA_ranking_calculator.hand
                        break
                    elif handA_sorted_remaining_values[card_index] < handB_sorted_remaining_values[card_index]:
                        winning_hand = self.handB_ranking_calculator.hand
                        break
        elif self.handA_ranking_calculator.is_high_card() and not self.handB_ranking_calculator.is_high_card():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_high_card() and self.handB_ranking_calculator.is_high_card():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_high_card() and self.handB_ranking_calculator.is_high_card():
            handA_sorted_values = list(sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True))
            handB_sorted_values = list(sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards], reverse=True))
            winning_hand = None
            for card_index in range(0, 5):
                if handA_sorted_values[card_index] > handB_sorted_values[card_index]:
                    winning_hand = self.handA_ranking_calculator.hand
                    break
                elif handA_sorted_values[card_index] < handB_sorted_values[card_index]:
                    winning_hand = self.handB_ranking_calculator.hand
                    break
        else:
            winning_hand = None
        return winning_hand






