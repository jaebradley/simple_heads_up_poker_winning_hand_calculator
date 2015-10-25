from unittest import TestCase
from src.model.hand_ranking import TwoPair
from src.impl.hand_ranking_calculator import TwoPairCalculator
from utils import two_pair_hand


class TestTwoPairCalculator(TestCase):
    def test_expected(self):
        two_pair_result = TwoPairCalculator.calculate_hand_ranking(two_pair_hand)

        self.assertIsNotNone(two_pair_result)
        self.assertTrue(isinstance(two_pair_result, TwoPair))
        self.assertTrue(two_pair_result.highest_pair_value == 3)
        self.assertTrue(two_pair_result.lowest_pair_value == 2)
        self.assertTrue(two_pair_result.kicker_value == 5)