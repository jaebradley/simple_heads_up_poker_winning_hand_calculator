from src.interfaces.heads_up_equivalent_hand_ranking_result_calculator import HeadsUpEquivalentHandRankingResultCalculatorInterface
from src.model.heads_up_result import HeadsUpResult
from src.model.heads_up_hand_rankings import HeadsUpHandRankings
from src.model.hand_ranking import HighCard, OnePair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush


class StraightFlushesResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):

    def calculate_result(self, heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)
        
        if isinstance(heads_up_hand_rankings.first_hand_ranking, StraightFlush) and isinstance(heads_up_hand_rankings.second_hand_ranking, StraightFlush):
            if heads_up_hand_rankings.first_hand_ranking.high_value > heads_up_hand_rankings.second_hand_ranking.high_value:
                result = HeadsUpResult.FirstHand
            elif heads_up_hand_rankings.first_hand_ranking.high_value < heads_up_hand_rankings.second_hand_ranking.high_value:
                result = HeadsUpResult.SecondHand
            else:
                result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    def __init__(self):
        HeadsUpEquivalentHandRankingResultCalculatorInterface.__init__(self)


class FourOfAKindsResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):

    def calculate_result(self, heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)
        if isinstance(heads_up_hand_rankings.first_hand_ranking, FourOfAKind) and isinstance(heads_up_hand_rankings.second_hand_ranking, FourOfAKind):
            if heads_up_hand_rankings.first_hand_ranking.four_of_a_kind_value > heads_up_hand_rankings.second_hand_ranking.four_of_a_kind_value:
                result = HeadsUpResult.FirstHand
            elif heads_up_hand_rankings.first_hand_ranking.four_of_a_kind_value < heads_up_hand_rankings.second_hand_ranking.four_of_a_kind_value:
                result = HeadsUpResult.SecondHand
            else:
                if heads_up_hand_rankings.first_hand_ranking.kicker_value > heads_up_hand_rankings.second_hand_ranking.kicker_value:
                    result = HeadsUpResult.FirstHand
                elif heads_up_hand_rankings.first_hand_ranking.kicker_value < heads_up_hand_rankings.second_hand_ranking.kicker_value:
                    result = HeadsUpResult.SecondHand
                else:
                    result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")
    
    def __init__(self):
        HeadsUpEquivalentHandRankingResultCalculatorInterface.__init__(self)


class FullHousesResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):

    def calculate_result(self, heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)
        
        if isinstance(heads_up_hand_rankings.first_hand_ranking, FullHouse) and isinstance(heads_up_hand_rankings.second_hand_ranking, FullHouse):
            if heads_up_hand_rankings.first_hand_ranking.three_of_a_kind_value > heads_up_hand_rankings.second_hand_ranking.three_of_a_kind_value:
                result = HeadsUpResult.FirstHand
            elif heads_up_hand_rankings.first_hand_ranking.three_of_a_kind_value < heads_up_hand_rankings.second_hand_ranking.three_of_a_kind_value:
                result = HeadsUpResult.SecondHand
            else:
                if heads_up_hand_rankings.first_hand_ranking.two_of_a_kind_value > heads_up_hand_rankings.second_hand_ranking.two_of_a_kind_value:
                    result = HeadsUpResult.FirstHand
                elif heads_up_hand_rankings.first_hand_ranking.two_of_a_kind_value < heads_up_hand_rankings.second_hand_ranking.two_of_a_kind_value:
                    result = HeadsUpResult.SecondHand
                else:
                    result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")
    
    def __init__(self):
        HeadsUpEquivalentHandRankingResultCalculatorInterface.__init__(self)
        

class FlushesResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):
    def calculate_result(self, heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)

        if isinstance(first_hand_ranking, Flush) and isinstance(second_hand_ranking, Flush):
            if first_hand_ranking.first_kicker > second_hand_ranking.first_kicker:
                result = HeadsUpResult.FirstHand
            elif first_hand_ranking.first_kicker < second_hand_ranking.first_kicker:
                result = HeadsUpResult.SecondHand
            else:
                if first_hand_ranking.second_kicker > second_hand_ranking.second_kicker:
                    result = HeadsUpResult.FirstHand
                elif first_hand_ranking.second_kicker < second_hand_ranking.second_kicker:
                    result = HeadsUpResult.SecondHand
                else:
                    if first_hand_ranking.third_kicker > second_hand_ranking.third_kicker:
                        result = HeadsUpResult.FirstHand
                    elif first_hand_ranking.third_kicker < second_hand_ranking.third_kicker:
                        result = HeadsUpResult.SecondHand
                    else:
                        if first_hand_ranking.fourth_kicker > second_hand_ranking.fourth_kicker:
                            result = HeadsUpResult.FirstHand
                        elif first_hand_ranking.fourth_kicker < second_hand_ranking.fourth_kicker:
                            result = HeadsUpResult.SecondHand
                        else:
                            if first_hand_ranking.fifth_kicker > second_hand_ranking.fifth_kicker:
                                result = HeadsUpResult.FirstHand
                            elif first_hand_ranking < second_hand_ranking.fifth_kicker:
                                result = HeadsUpResult.SecondHand
                            else:
                                result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    def __init__(self):
        HeadsUpEquivalentHandRankingResultCalculatorInterface.__init__(self)