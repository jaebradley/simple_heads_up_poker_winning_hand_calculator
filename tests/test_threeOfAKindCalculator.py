from unittest import TestCase
from src.model.hand_ranking import ThreeOfAKind
from src.impl.hand_ranking_calculator import ThreeOfAKindCalculator
from utils import three_of_a_kind_hand


class TestThreeOfAKindCalculator(TestCase):
    def test_expected(self):
        three_of_a_kind_result = ThreeOfAKindCalculator.calculate_hand_ranking(three_of_a_kind_hand)

        self.assertIsNotNone(three_of_a_kind_result)
        self.assertTrue(isinstance(three_of_a_kind_result, ThreeOfAKind))
        self.assertTrue(three_of_a_kind_result.three_of_a_kind_value == 3)
        self.assertTrue(three_of_a_kind_result.first_kicker_value == 14)
        self.assertTrue(three_of_a_kind_result.second_kicker_value == 2)