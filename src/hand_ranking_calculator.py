from collections import Counter


class HandRankingCalculator:

    def __init__(self, hand):
        self.hand = hand

    def is_flush(self):
        if [card.suit for card in self.hand.cards][1:] == [card.suit for card in self.hand.cards][:-1]:
            return True
        else:
            return False

    def is_high_value_straight(self):
        sorted_cards_by_high_value = sorted([card.high_value for card in self.hand.cards], reverse=True)
        is_consecutive_card_high_values = True
        for card_index in range(0, 4):
            if sorted_cards_by_high_value[card_index] - 1 != sorted_cards_by_high_value[card_index + 1]:
                is_consecutive_card_high_values = False
        if is_consecutive_card_high_values:
            return True
        else:
            return False

    def is_low_value_straight(self):
        sorted_cards_by_low_value = sorted([card.low_value for card in self.hand.cards], reverse=True)
        is_consecutive_card_low_values = True
        for card_index in range(0, 4):
            if sorted_cards_by_low_value[card_index] - 1 != sorted_cards_by_low_value[card_index + 1]:
                is_consecutive_card_low_values = False
        if is_consecutive_card_low_values:
            return True
        else:
            return False

    def is_straight(self):
        if self.is_high_value_straight() or self.is_low_value_straight():
            return True
        else:
            return False

    def is_straight_flush(self):

        if self.is_flush() and self.is_straight():
            return True
        else:
            return False

    def is_four_of_a_kind(self):
        card_values = [card.high_value for card in self.hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 2 and (card_counter[card_values[0]] == 4 or card_counter[card_values[0]] == 1):
            return True
        else:
            return False

    def is_full_house(self):
        card_values = [card.high_value for card in self.hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 2 and (card_counter[card_values[0]] == 3 or card_counter[card_values[0]] == 2):
            return True
        else:
            return False

    def is_three_of_a_kind(self):
        card_values = [card.high_value for card in self.hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 3 and (card_counter[card_values[0]] == 3 or card_counter[card_values[1]] == 3 or card_counter[distinct_card_values[2]] == 3):
            return True
        else:
            return False

    def is_two_pair(self):
        card_values = [card.high_value for card in self.hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 3 and (card_counter[card_values[0]] == 2 or card_counter[card_values[1]] == 2 or card_counter[card_values[2]] == 2):
            return True
        else:
            return False

    def is_one_pair(self):
        distinct_card_values = list(set([card.high_value for card in self.hand.cards]))
        if distinct_card_values.__len__() == 4:
            return True
        else:
            return False

    def is_high_card(self):
        distinct_card_values = list(set([card.high_value for card in self.hand.cards]))
        if not self.is_straight() and not self.is_flush() and distinct_card_values.__len__() == 5:
            return True
        else:
            return False
