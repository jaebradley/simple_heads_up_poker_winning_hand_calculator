from unittest import TestCase
from src.model.hand_ranking import HighCard
from src.impl.hand_ranking_calculator import HighCardCalculator
from utils import high_card_hand, low_straight_hand


class TestHighCardCalculator(TestCase):
    def test_expected(self):
        high_card_result = HighCardCalculator.calculate_hand_ranking(high_card_hand)

        self.assertIsNotNone(high_card_result)
        self.assertTrue(isinstance(high_card_result, HighCard))
        self.assertTrue(high_card_result.high_card_value == 14)
        self.assertTrue(high_card_result.first_kicker_value == 13)
        self.assertTrue(high_card_result.second_kicker_value == 12)
        self.assertTrue(high_card_result.third_kicker_value == 11)
        self.assertTrue(high_card_result.fourth_kicker_value == 2)

        self.assertRaises(RuntimeError, HighCardCalculator.calculate_hand_ranking, low_straight_hand)
