from unittest import TestCase
from src.model.hand_ranking import Flush
from src.impl.hand_ranking_calculator import FlushCalculator
from utils import flush_hand
from src.model.suit import Suit


class TestFlushCalculator(TestCase):
    def test_expected(self):
        flush_result = FlushCalculator.calculate_hand_ranking(flush_hand)
        self.assertIsNotNone(flush_result)
        self.assertTrue(isinstance(flush_result, Flush))
        self.assertTrue(flush_result.suit == Suit.Clubs)
        self.assertTrue(flush_result.first_kicker == 13)
        self.assertTrue(flush_result.second_kicker == 11)
        self.assertTrue(flush_result.third_kicker == 4)
        self.assertTrue(flush_result.fourth_kicker == 3)
        self.assertTrue(flush_result.fifth_kicker == 2)