from unittest import TestCase
from src.model.hand_ranking import StraightFlush
from src.impl.hand_ranking_calculator import StraightFlushCalculator
from utils import low_straight_flush_hand, high_straight_flush_hand, high_card_hand
from src.model.suit import Suit


class TestStraightFlushCalculator(TestCase):
    def test_expected(self):
        low_straight_flush_result = StraightFlushCalculator.calculate_hand_ranking(low_straight_flush_hand)

        self.assertIsNotNone(low_straight_flush_result)
        self.assertTrue(isinstance(low_straight_flush_result, StraightFlush))
        self.assertTrue(low_straight_flush_result.high_value == 5)
        self.assertTrue(low_straight_flush_result.suit == Suit.Clubs)

        high_straight_flush_result = StraightFlushCalculator.calculate_hand_ranking(high_straight_flush_hand)

        self.assertIsNotNone(high_straight_flush_result)
        self.assertTrue(isinstance(high_straight_flush_result, StraightFlush))
        self.assertTrue(high_straight_flush_result.high_value == 14)
        self.assertTrue(high_straight_flush_result.suit == Suit.Clubs)

        self.assertRaises(RuntimeError, StraightFlushCalculator.calculate_hand_ranking, high_card_hand)