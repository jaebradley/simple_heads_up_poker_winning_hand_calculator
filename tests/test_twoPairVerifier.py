from unittest import TestCase
from src.impl.hand_ranking_verifier import TwoPairVerifier
from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit


class TestTwoPairVerifier(TestCase):
    def test_expected(self):
        two_pair_hand = Hand(
            [
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Three(Suit.Diamonds),
                Five(Suit.Clubs)
            ]
        )

        self.assertTrue(TwoPairVerifier.verify_hand_ranking(two_pair_hand))

        full_house_hand = Hand(
            [
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Three(Suit.Diamonds),
                Three(Suit.Clubs)
            ]
        )

        self.assertFalse(TwoPairVerifier.verify_hand_ranking(full_house_hand))

        three_of_a_kind_hand = Hand(
            [
                Ace(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Three(Suit.Diamonds),
                Three(Suit.Clubs)
            ]
        )

        self.assertFalse(TwoPairVerifier.verify_hand_ranking(three_of_a_kind_hand))

        one_pair_hand = Hand(
            [
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Four(Suit.Diamonds),
                Five(Suit.Clubs)
            ]
        )

        self.assertFalse(TwoPairVerifier.verify_hand_ranking(one_pair_hand))