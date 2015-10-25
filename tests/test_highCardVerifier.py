from unittest import TestCase
from src.impl.hand_ranking_verifier import HighCardVerifier
from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit


class TestHighCardVerifier(TestCase):
    def test_expected(self):
        high_card_hand = Hand(
            [
                Ace(Suit.Spades),
                Two(Suit.Clubs),
                King(Suit.Hearts),
                Queen(Suit.Diamonds),
                Jack(Suit.Hearts)
            ]
        )

        self.assertTrue(HighCardVerifier.verify_hand_ranking(high_card_hand))

        one_pair_hand = Hand(
            [
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Four(Suit.Diamonds),
                Five(Suit.Hearts)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(one_pair_hand))

        two_pair_hand = Hand(
            [
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Three(Suit.Diamonds),
                Five(Suit.Clubs)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(two_pair_hand))

        full_house_hand = Hand(
            [
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Three(Suit.Diamonds),
                Three(Suit.Clubs)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(full_house_hand))

        three_of_a_kind_hand = Hand(
            [
                Ace(Suit.Clubs),
                Two(Suit.Diamonds),
                Three(Suit.Clubs),
                Three(Suit.Diamonds),
                Three(Suit.Clubs)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(three_of_a_kind_hand))

        four_of_a_kind_hand = Hand(
            [
                Two(Suit.Clubs),
                Two(Suit.Diamonds),
                Two(Suit.Hearts),
                Two(Suit.Spades),
                Ace(Suit.Spades)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(four_of_a_kind_hand))

        low_straight_hand = Hand(
            [
                Ace(Suit.Spades),
                Two(Suit.Clubs),
                Three(Suit.Hearts),
                Four(Suit.Spades),
                Five(Suit.Diamonds)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(low_straight_hand))

        high_straight_hand = Hand(
            [
                Ace(Suit.Spades),
                Jack(Suit.Diamonds),
                King(Suit.Clubs),
                Ten(Suit.Hearts),
                Queen(Suit.Clubs)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(high_straight_hand))

        flush_hand = Hand(
            [
                Two(Suit.Clubs),
                Three(Suit.Clubs),
                Four(Suit.Clubs),
                Jack(Suit.Clubs),
                King(Suit.Clubs)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(flush_hand))

        low_straight_flush_hand = Hand(
            [
                Ace(Suit.Clubs),
                Two(Suit.Clubs),
                Three(Suit.Clubs),
                Four(Suit.Clubs),
                Five(Suit.Clubs)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(low_straight_flush_hand))

        high_straight_flush_hand = Hand(
            [
                Ace(Suit.Clubs),
                Queen(Suit.Clubs),
                Ten(Suit.Clubs),
                King(Suit.Clubs),
                Jack(Suit.Clubs)
            ]
        )

        self.assertFalse(HighCardVerifier.verify_hand_ranking(high_straight_flush_hand))