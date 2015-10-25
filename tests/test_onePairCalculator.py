from unittest import TestCase
from src.model.hand_ranking import OnePair
from src.impl.hand_ranking_calculator import OnePairCalculator
from utils import one_pair_hand


class TestOnePairCalculator(TestCase):
    def test_expected(self):
        one_pair_result = OnePairCalculator.calculate_hand_ranking(one_pair_hand)

        self.assertIsNotNone(one_pair_result)
        self.assertTrue(isinstance(one_pair_result, OnePair))
        self.assertTrue(one_pair_result.pair_value == 2)
        self.assertTrue(one_pair_result.first_kicker_value == 5)
        self.assertTrue(one_pair_result.second_kicker_value == 4)
        self.assertTrue(one_pair_result.third_kicker_value == 3)