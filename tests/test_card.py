from src.model import Card, Suit
import unittest


class CardTest(unittest.TestCase):

    def test_expected_behavior(self):
        test_card = Card(
            5,
            5,
            Suit.Hearts
        )

        self.assertEquals(5, test_card.high_value)
        self.assertEquals(5, test_card.low_value)
        self.assertEquals(Suit.Hearts, test_card.suit)

    def test_high_value_assertion(self):
        try:
            Card(
                -1,
                5,
                Suit.Hearts
            )
            raise RuntimeError("should not reach")
        except AssertionError:
            pass

        try:
            Card(
                0,
                5,
                Suit.Hearts
            )
            raise RuntimeError("should not reach")
        except AssertionError:
            pass

        try:
            Card(
                1,
                5,
                Suit.Hearts
            )
            raise RuntimeError("should not reach")
        except AssertionError:
            pass

        try:
            Card(
                14,
                5,
                Suit.Hearts
            )
            raise RuntimeError("should not reach")
        except AssertionError:
            pass

    def test_low_value_assertion(self):
        try:
            Card(
                5,
                -1,
                Suit.Hearts
            )
            raise RuntimeError("should not reach")
        except AssertionError:
            pass

        try:
            Card(
                5,
                0,
                Suit.Hearts
            )
            raise RuntimeError("should not reach")
        except AssertionError:
            pass

        try:
            Card(
                5,
                13,
                Suit.Hearts
            )
            raise RuntimeError("should not reach")
        except AssertionError:
            pass