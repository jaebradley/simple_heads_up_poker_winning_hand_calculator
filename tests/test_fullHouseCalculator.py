from unittest import TestCase
from src.model.hand_ranking import FullHouse
from src.impl.hand_ranking_calculator import FullHouseCalculator
from utils import full_house_hand, three_of_a_kind_hand


class TestFullHouseCalculator(TestCase):
    def test_expected(self):
        full_house_result = FullHouseCalculator.calculate_hand_ranking(full_house_hand)

        self.assertIsNotNone(full_house_result)
        self.assertTrue(isinstance(full_house_result, FullHouse))
        self.assertTrue(full_house_result.two_of_a_kind_value == 2)
        self.assertTrue(full_house_result.three_of_a_kind_value == 3)

        self.assertRaises(RuntimeError, FullHouseCalculator.calculate_hand_ranking, three_of_a_kind_hand)