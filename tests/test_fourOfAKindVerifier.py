from unittest import TestCase
from src.impl.hand_ranking_verifier import FourOfAKindVerifier
from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit


class TestFourOfAKindVerifier(TestCase):
    def test_expected(self):
        four_of_a_kind_hand = Hand(
            [
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Two(Suit.Hearts),
                Two(Suit.Spades),
                Ace(Suit.Spades)
            ]
        )

        self.assertTrue(FourOfAKindVerifier.verify_hand_ranking(four_of_a_kind_hand))

        not_four_of_a_kind_hand = Hand(
            [
                Two(Suit.Clubs),
                Two(Suit.Spades),
                Two(Suit.Hearts),
                Three(Suit.Hearts),
                Four(Suit.Hearts)
            ]
        )

        self.assertFalse(FourOfAKindVerifier.verify_hand_ranking(not_four_of_a_kind_hand))