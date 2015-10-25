from unittest import TestCase
from src.impl.hand_ranking_verifier import StraightVerifier
from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit


class TestStraightVerifier(TestCase):
    def test_expected(self):
        low_straight_hand = Hand(
            [
                Ace(Suit.Spades),
                Two(Suit.Clubs),
                Three(Suit.Hearts),
                Four(Suit.Spades),
                Five(Suit.Diamonds)
            ]
        )

        self.assertTrue(StraightVerifier.verify_hand_ranking(low_straight_hand))

        high_straight_hand = Hand(
            [
                Ace(Suit.Spades),
                Jack(Suit.Diamonds),
                King(Suit.Clubs),
                Ten(Suit.Hearts),
                Queen(Suit.Clubs)
            ]
        )

        self.assertTrue(StraightVerifier.verify_hand_ranking(high_straight_hand))

        straight_flush_hand = Hand(
            [
                Ace(Suit.Spades),
                Jack(Suit.Spades),
                King(Suit.Spades),
                Ten(Suit.Spades),
                Queen(Suit.Spades)
            ]
        )

        self.assertTrue(StraightVerifier.verify_hand_ranking(straight_flush_hand))

        almost_straight_hand = Hand(
            [
                Two(Suit.Spades),
                Jack(Suit.Spades),
                King(Suit.Spades),
                Ten(Suit.Spades),
                Queen(Suit.Spades)
            ]
        )

        self.assertFalse(StraightVerifier.verify_hand_ranking(almost_straight_hand))