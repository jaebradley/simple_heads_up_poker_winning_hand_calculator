from collections import Counter
from model import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace


class HandRankingCalculator:

    def __init__(self):
        pass

    @staticmethod
    def is_flush(hand):
        if 1 == len(set([card.suit for card in hand.cards])):
            return True
        else:
            return False

    @staticmethod
    def is_straight(hand):
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

    @staticmethod
    def is_straight_flush(hand):
        if HandRankingCalculator.is_flush(hand) and HandRankingCalculator.is_straight(hand):
            return True
        else:
            return False

    @staticmethod
    def is_four_of_a_kind(hand):
        card_values = [card.value for card in hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 2 and (card_counter[card_values[0]] == 4 or card_counter[card_values[0]] == 1):
            return True
        else:
            return False

    @staticmethod
    def is_full_house(hand):
        card_values = [card.high_value for card in hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 2 and (card_counter[card_values[0]] == 3 or card_counter[card_values[0]] == 2):
            return True
        else:
            return False

    @staticmethod
    def is_three_of_a_kind(hand):
        card_values = [card.high_value for card in hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 3 and (card_counter[card_values[0]] == 3 or card_counter[card_values[1]] == 3 or card_counter[distinct_card_values[2]] == 3):
            return True
        else:
            return False

    @staticmethod
    def is_two_pair(hand):
        card_values = [card.high_value for card in hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 3 and (card_counter[card_values[0]] == 2 or card_counter[card_values[1]] == 2 or card_counter[card_values[2]] == 2):
            return True
        else:
            return False

    @staticmethod
    def is_one_pair(hand):
        distinct_card_values = list(set([card.high_value for card in hand.cards]))
        if distinct_card_values.__len__() == 4:
            return True
        else:
            return False

    @staticmethod
    def is_high_card(hand):
        distinct_card_values = list(set([card.high_value for card in hand.cards]))
        if not HandRankingCalculator.is_straight(hand) and not HandRankingCalculator.is_flush(hand) and distinct_card_values.__len__() == 5:
            return True
        else:
            return False

    @staticmethod
    def return_calculated_hand_ranking(hand):
        if is_straight_flush(hand):
            return