from unittest import TestCase
from src.impl.hand_ranking_verifier import FlushVerifier
from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit


class TestFlushVerifier(TestCase):
    def test_expected(self):
        flush_hand = Hand(
            [
                Two(Suit.Clubs),
                Three(Suit.Clubs),
                Four(Suit.Clubs),
                Jack(Suit.Clubs),
                King(Suit.Clubs)
            ]
        )

        is_flush_result = FlushVerifier.verify_hand_ranking(flush_hand)

        self.assertTrue(is_flush_result)

        non_flush_hand = Hand(
            [
                Two(Suit.Hearts),
                Three(Suit.Clubs),
                Four(Suit.Clubs),
                Jack(Suit.Clubs),
                King(Suit.Clubs)
            ]
        )

        is_not_flush_result = FlushVerifier.verify_hand_ranking(non_flush_hand)

        self.assertFalse(is_not_flush_result)