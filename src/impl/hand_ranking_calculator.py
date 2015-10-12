from collections import Counter
from src.model.card import Two, Three, Four, Five, Ace
from src.model.hand_ranking import HighCard, OnePair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush


class HandRankingCalculator:

    def __init__(self):
        pass

    @staticmethod
    def calculate_straight_flush(hand):
        if HandRankingCalculator.is_straight_flush(hand):
            high_card_value = 0
            high_card = None
            for card in hand.cards:
                if card.value > high_card_value:
                    high_card = card
            return StraightFlush(high_card)
        else:
            return False

    @staticmethod
    def calculate_four_of_a_kind(hand):
        if HandRankingCalculator.is_four_of_a_kind(hand):
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
            return False

    @staticmethod
    def calculate_full_house(hand):
        if HandRankingCalculator.is_full_house(hand):
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
            return False

    @staticmethod
    def calculate_straight(hand):
        if HandRankingCalculator.is_straight(hand):
            high_value = sorted([card.value for card in hand.cards], reverse=True)[0]
            return Straight(high_value)
        else:
            return False

    @staticmethod
    def calculate_flush(hand):
        if HandRankingCalculator.is_flush(hand):
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
            return False

    @staticmethod
    def calculate_three_of_a_kind(hand):
        if HandRankingCalculator.is_three_of_a_kind(hand):
            three_of_a_kind_value = max(set(hand.cards), key=hand.cards.count).high_value
            sorted_card_values = sorted([card.value for card in hand.cards if card.value != three_of_a_kind_value], reverse=True)
            first_kicker_value = sorted_card_values[0]
            second_kicker_value = sorted_card_values[1]
            return ThreeOfAKind(
                three_of_a_kind_value,
                first_kicker_value,
                second_kicker_value
            )
        else:
            return False

    @staticmethod
    def calculate_two_pair(hand):
        if HandRankingCalculator.is_two_pair(hand):
            hand_value_counter = Counter([card.high_value for card in hand.cards])
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
            return False

    @staticmethod
    def calculate_one_pair(hand):
        if HandRankingCalculator.is_one_pair(hand):
            hand_value_counter = Counter([card.high_value for card in hand.cards])
            hand_most_common_values = hand_value_counter.most_common()
            pair_value = hand_most_common_values[0][0]
            return OnePair(
                pair_value,
                hand_most_common_values[1][0],
                hand_most_common_values[2][0],
                hand_most_common_values[3][0]
            )

    @staticmethod
    def calculate_high_card(hand):
        if HandRankingCalculator.is_high_card(hand):
            sorted_card_values = sorted([card.value for card in hand.cards], reverse=True)
            return HighCard(
                sorted_card_values[0],
                sorted_card_values[1],
                sorted_card_values[2],
                sorted_card_values[3],
                sorted_card_values[4]
            )
        else:
            return False

    @staticmethod
    def calculate_hand_ranking(hand):
        straight_flush_calculation = HandRankingCalculator.calculate_straight_flush(hand)
        if isinstance(straight_flush_calculation, StraightFlush):
            return straight_flush_calculation
        else:
            four_of_a_kind_calculation = HandRankingCalculator.calculate_four_of_a_kind(hand)
            if isinstance(four_of_a_kind_calculation, FourOfAKind):
                return four_of_a_kind_calculation
            else:
                full_house_calculation = HandRankingCalculator.calculate_full_house(hand)
                if isinstance(full_house_calculation, FullHouse):
                    return full_house_calculation
                else:
                    flush_calculation = HandRankingCalculator.calculate_flush(hand)
                    if isinstance(flush_calculation, Flush):
                        return flush_calculation
                    else:
                        straight_calculation = HandRankingCalculator.calculate_straight(hand)
                        if isinstance(straight_calculation, Straight):
                            return straight_calculation
                        else:
                            three_of_a_kind_calculation = HandRankingCalculator.calculate_three_of_a_kind(hand)
                            if isinstance(three_of_a_kind_calculation, ThreeOfAKind):
                                return three_of_a_kind_calculation
                            else:
                                two_pair_calculation = HandRankingCalculator.calculate_two_pair(hand)
                                if isinstance(two_pair_calculation, TwoPair):
                                    return two_pair_calculation
                                else:
                                    one_pair_calculation = HandRankingCalculator.calculate_one_pair(hand)
                                    if isinstance(one_pair_calculation, OnePair):
                                        return one_pair_calculation
                                    else:
                                        high_card_calculation = HandRankingCalculator.calculate_high_card(hand)
                                        if isinstance(high_card_calculation, HighCard):
                                            return high_card_calculation
                                        else:
                                            raise ValueError("can not calculate hand ranking")