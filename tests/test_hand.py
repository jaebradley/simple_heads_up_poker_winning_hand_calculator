from src.model import Hand, Card, Suit
import unittest


class HandTest(unittest.TestCase):

    def test_expected_behavior(self):
        cards = list()
        for card_value in range(2, 7):
            cards.append(Card(card_value, card_value, Suit.Clubs))
        test_hand = Hand(cards)
        self.assertEquals(cards, test_hand.cards)

    def test_card_size_assertion(self):
        cards = list()
        for card_value in range(2, 6):
            cards.append(Card(card_value, card_value, Suit.Clubs))
        try:
            Hand(cards)
            raise RuntimeError("should not reach")
        except AssertionError:
            pass

        cards = list()
        for card_value in range(2, 8):
            cards.append(Card(card_value, card_value, Suit.Clubs))
        try:
            Hand(cards)
            raise RuntimeError("should not reach")
        except AssertionError:
            pass
