from unittest import TestCase
from src.impl.hand_ranking_verifier import StraightFlushVerifier
from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit


class TestStraightFlushVerifier(TestCase):
    def test_expected(self):
        low_straight_flush_hand = Hand(
            [
                Ace(Suit.Clubs),
                Two(Suit.Clubs),
                Three(Suit.Clubs),
                Four(Suit.Clubs),
                Five(Suit.Clubs)
            ]
        )

        self.assertTrue(StraightFlushVerifier.verify_hand_ranking(low_straight_flush_hand))

        high_straight_flush_hand = Hand(
            [
                Ace(Suit.Clubs),
                Queen(Suit.Clubs),
                Ten(Suit.Clubs),
                King(Suit.Clubs),
                Jack(Suit.Clubs)
            ]
        )

        self.assertTrue(StraightFlushVerifier.verify_hand_ranking(high_straight_flush_hand))

        straight_hand = Hand(
            [
                Ace(Suit.Hearts),
                Queen(Suit.Clubs),
                Ten(Suit.Clubs),
                King(Suit.Diamonds),
                Jack(Suit.Clubs)
            ]
        )

        self.assertFalse(StraightFlushVerifier.verify_hand_ranking(straight_hand))

        flush_hand = Hand(
            [
                Ace(Suit.Clubs),
                Three(Suit.Clubs),
                Ten(Suit.Clubs),
                King(Suit.Clubs),
                Jack(Suit.Clubs)
            ]
        )

        self.assertFalse(StraightFlushVerifier.verify_hand_ranking(flush_hand))