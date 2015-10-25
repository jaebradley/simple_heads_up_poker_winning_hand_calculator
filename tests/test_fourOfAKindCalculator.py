from unittest import TestCase
from src.model.hand_ranking import FourOfAKind
from src.impl.hand_ranking_calculator import FourOfAKindCalculator
from utils import four_of_a_kind_hand, three_of_a_kind_hand


class TestFourOfAKindCalculator(TestCase):
    def test_expected(self):
        four_of_a_kind_result = FourOfAKindCalculator.calculate_hand_ranking(four_of_a_kind_hand)

        self.assertIsNotNone(four_of_a_kind_result)
        self.assertTrue(isinstance(four_of_a_kind_result, FourOfAKind))
        self.assertTrue(four_of_a_kind_result.four_of_a_kind_value == 2)
        self.assertTrue(four_of_a_kind_result.kicker_value == 14)

        self.assertRaises(RuntimeError, FourOfAKindCalculator.calculate_hand_ranking, three_of_a_kind_hand)