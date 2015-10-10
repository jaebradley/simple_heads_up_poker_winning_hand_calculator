from src.model.heads_up import HeadsUp
from src.interfaces.heads_up_result_calculator import HeadsUpResultCalculatorInterface
from src.impl.hand_ranking_calculator import HandRankingCalculator
from src.model.heads_up_hand_rankings import HeadsUpHandRankings
from src.impl.heads_up_equivalent_hand_ranking_result_calculators import HighCardsResultCalculator, OnePairsResultCalculator, TwoPairsResultCalculator, ThreeOfAKindsResultCalculator, StraightsResultCalculator, FlushesResultCalculator, FullHousesResultCalculator, FourOfAKindsResultCalculator, StraightFlushesResultCalculator
from src.impl.heads_up_different_hand_ranking_result_calculator import HeadsUpDifferentHandRankingResultCalculator
from src.model.hand_ranking import HighCard, OnePair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush


class HeadsUpResultCalculator(HeadsUpResultCalculatorInterface):

    @staticmethod
    def calculate_result(heads_up):

        assert isinstance(heads_up, HeadsUp)

        heads_up_hand_rankings = HeadsUpHandRankings(
            HandRankingCalculator.calculate_hand_ranking(heads_up.first_hand),
            HandRankingCalculator.calculate_hand_ranking(heads_up.second_hand)
        )

        if not heads_up_hand_rankings.are_same_hand_rankings():
            different_hand_calculator = HeadsUpDifferentHandRankingResultCalculator()
            result = different_hand_calculator.calculate_result(heads_up_hand_rankings)
        else:
            if isinstance(heads_up_hand_rankings.first_hand_ranking, StraightFlush):
                result = StraightFlushesResultCalculator.calculate_result(heads_up_hand_rankings)

            elif isinstance(heads_up_hand_rankings.first_hand_ranking, FourOfAKind):
                result = FourOfAKindsResultCalculator.calculate_result(heads_up_hand_rankings)

            elif isinstance(heads_up_hand_rankings.first_hand_ranking, FullHouse):
                result = FullHousesResultCalculator.calculate_result(heads_up_hand_rankings)

            elif isinstance(heads_up_hand_rankings.first_hand_ranking, Flush):
                result = FlushesResultCalculator.calculate_result(heads_up_hand_rankings)

            elif isinstance(heads_up_hand_rankings.first_hand_ranking, Straight):
                result = StraightsResultCalculator.calculate_result(heads_up_hand_rankings)

            elif isinstance(heads_up_hand_rankings.first_hand_ranking, ThreeOfAKind):
                result = ThreeOfAKindsResultCalculator.calculate_result(heads_up_hand_rankings)

            elif isinstance(heads_up_hand_rankings.first_hand_ranking, TwoPair):
                result = TwoPairsResultCalculator.calculate_result(heads_up_hand_rankings)

            elif isinstance(heads_up_hand_rankings.first_hand_ranking, OnePair):
                result = OnePairsResultCalculator.calculate_result(heads_up_hand_rankings)

            elif isinstance(heads_up_hand_rankings.first_hand_ranking, HighCard):
                result = HighCardsResultCalculator.calculate_result(heads_up_hand_rankings)

            else:
                raise RuntimeError("unexpected hand ranking")

        return result

    def __init__(self):
        HeadsUpResultCalculatorInterface.__init__(self)