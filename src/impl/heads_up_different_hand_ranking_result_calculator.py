from src.interfaces.heads_up_hand_ranking_result_calculator import HeadsUpHandRankingResultCalculatorInterface
from src.model.heads_up_hand_rankings import HeadsUpHandRankings
from src.model.heads_up_result import HeadsUpResult
from src.model.hand_ranking import HighCard, OnePair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush


class HeadsUpDifferentHandRankingResultCalculator(HeadsUpHandRankingResultCalculatorInterface):

    @staticmethod
    def calculate_result(heads_up_hand_rankings):

        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)

        if isinstance(heads_up_hand_rankings.first_hand_ranking, StraightFlush):
            result = HeadsUpResult.FirstHand
        elif isinstance(heads_up_hand_rankings.second_hand_ranking, StraightFlush):
            result = HeadsUpResult.SecondHand
        elif isinstance(heads_up_hand_rankings.first_hand_ranking, FourOfAKind):
            result = HeadsUpResult.FirstHand
        elif isinstance(heads_up_hand_rankings.second_hand_ranking, FourOfAKind):
            result = HeadsUpResult.SecondHand
        elif isinstance(heads_up_hand_rankings.first_hand_ranking, FullHouse):
            result = HeadsUpResult.FirstHand
        elif isinstance(heads_up_hand_rankings.second_hand_ranking, FullHouse):
            result = HeadsUpResult.SecondHand
        elif isinstance(heads_up_hand_rankings.first_hand_ranking, Flush):
            result = HeadsUpResult.FirstHand
        elif isinstance(heads_up_hand_rankings.second_hand_ranking, Flush):
            result = HeadsUpResult.SecondHand
        elif isinstance(heads_up_hand_rankings.first_hand_ranking, Straight):
            result = HeadsUpResult.FirstHand
        elif isinstance(heads_up_hand_rankings.second_hand_ranking, Straight):
            result = HeadsUpResult.SecondHand
        elif isinstance(heads_up_hand_rankings.first_hand_ranking, ThreeOfAKind):
            result = HeadsUpResult.FirstHand
        elif isinstance(heads_up_hand_rankings.second_hand_ranking, ThreeOfAKind):
            result = HeadsUpResult.SecondHand
        elif isinstance(heads_up_hand_rankings.first_hand_ranking, TwoPair):
            result = HeadsUpResult.FirstHand
        elif isinstance(heads_up_hand_rankings.second_hand_ranking, TwoPair):
            result = HeadsUpResult.SecondHand
        elif isinstance(heads_up_hand_rankings.first_hand_ranking, OnePair):
            result = HeadsUpResult.FirstHand
        elif isinstance(heads_up_hand_rankings.second_hand_ranking, OnePair):
            result = HeadsUpResult.SecondHand
        elif isinstance(heads_up_hand_rankings.first_hand_ranking, HighCard):
            result = HeadsUpResult.FirstHand
        elif isinstance(heads_up_hand_rankings.second_hand_ranking, HighCard):
            result = HeadsUpResult.SecondHand
        else:
            raise RuntimeError("unexpected heads up ranking")

        return result

    def __init__(self):
        HeadsUpHandRankingResultCalculatorInterface.__init__(self)
