from src.model.heads_up import HeadsUp
from src.interfaces.heads_up_result_calculator import HeadsUpResultCalculatorInterface
from src.impl.hand_ranking_calculator import HandRankingCalculator
from src.model.heads_up_hand_rankings import HeadsUpHandRankings
from src.impl.heads_up_equivalent_hand_ranking_result_calculators import StraightFlushesResultCalculator
from src.impl.heads_up_different_hand_ranking_result_calculator import HeadsUpDifferentHandRankingResultCalculator


class HeadsUpResultCalculator(HeadsUpResultCalculatorInterface):
    def calculate_result(self, heads_up):

        assert isinstance(heads_up, HeadsUp)

        first_hand_ranking = HandRankingCalculator.calculate_hand_ranking(heads_up.first_hand)
        second_hand_ranking = HandRankingCalculator.calculate_hand_ranking(heads_up.second_hand)

        heads_up_hand_rankings = HeadsUpHandRankings(
            first_hand_ranking,
            second_hand_ranking
        )

        if not heads_up_hand_rankings.are_same_hand_rankings():
            different_hand_calculator = HeadsUpDifferentHandRankingResultCalculator()
            result = different_hand_calculator.calculate_result(heads_up_hand_rankings)


        return result

    def __init__(self):
        HeadsUpResultCalculatorInterface.__init__(self)
