from unittest import TestCase
from src.model.hand_ranking import Straight
from src.impl.hand_ranking_calculator import StraightCalculator
from utils import low_straight_hand, high_straight_hand, low_straight_flush_hand, high_straight_flush_hand


class TestStraightCalculator(TestCase):
    def test_expected(self):
        low_straight_result = StraightCalculator.calculate_hand_ranking(low_straight_hand)

        self.assertIsNotNone(low_straight_result)
        self.assertTrue(isinstance(low_straight_result, Straight))
        self.assertTrue(low_straight_result.high_value, 5)

        high_straight_result = StraightCalculator.calculate_hand_ranking(high_straight_hand)

        self.assertIsNotNone(high_straight_result)
        self.assertTrue(isinstance(high_straight_result, Straight))
        self.assertTrue(high_straight_result.high_value, 14)

        self.assertRaises(RuntimeError, StraightCalculator.calculate_hand_ranking, low_straight_flush_hand)
        self.assertRaises(RuntimeError, StraightCalculator.calculate_hand_ranking, high_straight_flush_hand)