from unittest import TestCase
from src.impl.heads_up_result_calculator import HeadsUpResultCalculator
from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit
from src.model.heads_up import HeadsUp
from src. model.heads_up_result import HeadsUpResult


class TestHeadsUpResultCalculator(TestCase):

    def test_calculate_result(self):

        first_hand = Hand(
            [Two(Suit.Clubs), Two(Suit.Diamonds), Two(Suit.Hearts), Two(Suit.Spades), Three(Suit.Diamonds)]
        )

        second_hand = Hand(
            [Three(Suit.Clubs), Four(Suit.Diamonds), Five(Suit.Spades), Six(Suit.Hearts), Seven(Suit.Hearts)]
        )

        heads_up = HeadsUp(
            first_hand,
            second_hand
        )

        result = HeadsUpResultCalculator.calculate_result(heads_up)

        assert result == HeadsUpResult.FirstHand
