from src.interfaces.heads_up_hand_ranking_result_calculator import HeadsUpHandRankingResultCalculatorInterface


class HeadsUpEquivalentHandRankingResultCalculatorInterface(HeadsUpHandRankingResultCalculatorInterface):

    def calculate_result(self, heads_up_hand_rankings):
        pass

    def __init__(self):
        HeadsUpHandRankingResultCalculatorInterface.__init__(self)
        pass
