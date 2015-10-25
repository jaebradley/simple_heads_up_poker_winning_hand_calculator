from unittest import TestCase
from src.impl.hand_ranking_verifier import FullHouseVerifier
from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit


class TestFullHouseVerifier(TestCase):
    def test_expected(self):
        full_house_hand = Hand(
            [
                Two(Suit.Hearts),
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Three(Suit.Diamonds)
            ]
        )

        self.assertTrue(FullHouseVerifier.verify_hand_ranking(full_house_hand))

        four_of_a_kind_hand = Hand(
            [
                Two(Suit.Diamonds),
                Two(Suit.Clubs),
                Two(Suit.Hearts),
                Two(Suit.Spades),
                Three(Suit.Hearts)
            ]
        )

        self.assertFalse(FullHouseVerifier.verify_hand_ranking(four_of_a_kind_hand))

        three_of_a_kind_hand = Hand(
            [
                Two(Suit.Hearts),
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Four(Suit.Diamonds)
            ]
        )

        self.assertFalse(FullHouseVerifier.verify_hand_ranking(three_of_a_kind_hand))

        two_of_a_kind_hand = Hand(
            [
                Ace(Suit.Hearts),
                Two(Suit.Clubs),
                Six(Suit.Diamonds),
                Three(Suit.Clubs),
                Three(Suit.Diamonds)
            ]
        )

        self.assertFalse(FullHouseVerifier.verify_hand_ranking(two_of_a_kind_hand))