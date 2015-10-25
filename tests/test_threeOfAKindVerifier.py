from unittest import TestCase
from src.impl.hand_ranking_verifier import ThreeOfAKindVerifier
from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit


class TestThreeOfAKindVerifier(TestCase):
    def test_expected(self):
        three_of_a_kind_hand = Hand(
            [
                Two(Suit.Hearts),
                Two(Suit.Spades),
                Two(Suit.Clubs),
                Four(Suit.Spades),
                Five(Suit.Clubs)
            ]
        )

        self.assertTrue(ThreeOfAKindVerifier.verify_hand_ranking(three_of_a_kind_hand))

        full_house_hand = Hand(
            [
                Two(Suit.Hearts),
                Two(Suit.Spades),
                Two(Suit.Clubs),
                Four(Suit.Spades),
                Four(Suit.Clubs)
            ]
        )

        self.assertFalse(ThreeOfAKindVerifier.verify_hand_ranking(full_house_hand))

        four_of_a_kind_hand = Hand(
            [
                Two(Suit.Hearts),
                Two(Suit.Spades),
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Four(Suit.Clubs)
            ]
        )

        self.assertFalse(ThreeOfAKindVerifier.verify_hand_ranking(four_of_a_kind_hand))