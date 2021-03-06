from src.interfaces.heads_up_equivalent_hand_ranking_result_calculator import HeadsUpEquivalentHandRankingResultCalculatorInterface
from src.model.heads_up_result import HeadsUpResult
from src.model.heads_up_hand_rankings import HeadsUpHandRankings
from src.model.hand_ranking import HighCard, OnePair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush


class StraightFlushesResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):

    @staticmethod
    def calculate_result(heads_up_hand_rankings):
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

    @staticmethod
    def calculate_result(heads_up_hand_rankings):
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

    @staticmethod
    def calculate_result(heads_up_hand_rankings):
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

    @staticmethod
    def calculate_result(heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)

        if isinstance(heads_up_hand_rankings.first_hand_ranking, Flush) and isinstance(heads_up_hand_rankings.second_hand_ranking, Flush):
            if heads_up_hand_rankings.first_hand_ranking.first_kicker > heads_up_hand_rankings.second_hand_ranking.first_kicker:
                result = HeadsUpResult.FirstHand
            elif heads_up_hand_rankings.first_hand_ranking.first_kicker < heads_up_hand_rankings.second_hand_ranking.first_kicker:
                result = HeadsUpResult.SecondHand
            else:
                if heads_up_hand_rankings.first_hand_ranking.second_kicker > heads_up_hand_rankings.second_hand_ranking.second_kicker:
                    result = HeadsUpResult.FirstHand
                elif heads_up_hand_rankings.first_hand_ranking.second_kicker < heads_up_hand_rankings.second_hand_ranking.second_kicker:
                    result = HeadsUpResult.SecondHand
                else:
                    if heads_up_hand_rankings.first_hand_ranking.third_kicker > heads_up_hand_rankings.second_hand_ranking.third_kicker:
                        result = HeadsUpResult.FirstHand
                    elif heads_up_hand_rankings.first_hand_ranking.third_kicker < heads_up_hand_rankings.second_hand_ranking.third_kicker:
                        result = HeadsUpResult.SecondHand
                    else:
                        if heads_up_hand_rankings.first_hand_ranking.fourth_kicker > heads_up_hand_rankings.second_hand_ranking.fourth_kicker:
                            result = HeadsUpResult.FirstHand
                        elif heads_up_hand_rankings.first_hand_ranking.fourth_kicker < heads_up_hand_rankings.second_hand_ranking.fourth_kicker:
                            result = HeadsUpResult.SecondHand
                        else:
                            if heads_up_hand_rankings.first_hand_ranking.fifth_kicker > heads_up_hand_rankings.second_hand_ranking.fifth_kicker:
                                result = HeadsUpResult.FirstHand
                            elif heads_up_hand_rankings.first_hand_ranking < heads_up_hand_rankings.second_hand_ranking.fifth_kicker:
                                result = HeadsUpResult.SecondHand
                            else:
                                result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    def __init__(self):
        HeadsUpEquivalentHandRankingResultCalculatorInterface.__init__(self)
        

class StraightsResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):

    @staticmethod
    def calculate_result(heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)
        
        if isinstance(heads_up_hand_rankings.first_hand_ranking, Straight) and isinstance(heads_up_hand_rankings.second_hand_ranking, Straight):
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
        

class ThreeOfAKindsResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):

    @staticmethod
    def calculate_result(heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)
        
        if isinstance(heads_up_hand_rankings.first_hand_ranking, ThreeOfAKind) and isinstance(heads_up_hand_rankings.second_hand_ranking, ThreeOfAKind):
            if heads_up_hand_rankings.first_hand_ranking.three_of_a_kind_value > heads_up_hand_rankings.second_hand_ranking.three_of_a_kind_value:
                result = HeadsUpResult.FirstHand
            elif heads_up_hand_rankings.first_hand_ranking.three_of_a_kind_value < heads_up_hand_rankings.second_hand_ranking.three_of_a_kind_value:
                result = HeadsUpResult.SecondHand
            else:
                if heads_up_hand_rankings.first_hand_ranking.first_kicker_value > heads_up_hand_rankings.second_hand_ranking.first_kicker_value:
                    result = HeadsUpResult.FirstHand
                elif heads_up_hand_rankings.first_hand_ranking.first_kicker_value < heads_up_hand_rankings.second_hand_ranking.first_kicker_value:
                    result = HeadsUpResult.SecondHand
                else:
                    if heads_up_hand_rankings.first_hand_ranking.second_kicker_value > heads_up_hand_rankings.second_hand_ranking.second_kicker_value:
                        result = HeadsUpResult.FirstHand
                    elif heads_up_hand_rankings.first_hand_ranking < heads_up_hand_rankings.second_hand_ranking.second_kicker_value:
                        result = HeadsUpResult.SecondHand
                    else:
                        result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    def __init__(self):
        HeadsUpEquivalentHandRankingResultCalculatorInterface.__init__(self)


class TwoPairsResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):

    @staticmethod
    def calculate_result(heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)

        if isinstance(heads_up_hand_rankings.first_hand_ranking, TwoPair) and isinstance(heads_up_hand_rankings.second_hand_ranking, TwoPair):
            if heads_up_hand_rankings.first_hand_ranking.highest_pair_value > heads_up_hand_rankings.second_hand_ranking.highest_pair_value:
                result = HeadsUpResult.FirstHand
            elif heads_up_hand_rankings.first_hand_ranking.highest_pair_value < heads_up_hand_rankings.second_hand_ranking.highest_pair_value:
                result = HeadsUpResult.SecondHand
            else:
                if heads_up_hand_rankings.first_hand_ranking.lowest_pair_value > heads_up_hand_rankings.second_hand_ranking.lowest_pair_value:
                    result = HeadsUpResult.FirstHand
                elif heads_up_hand_rankings.first_hand_ranking.lowest_pair_value < heads_up_hand_rankings.second_hand_ranking.lowest_pair_value:
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


class OnePairsResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):

    @staticmethod
    def calculate_result(heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)

        if isinstance(heads_up_hand_rankings.first_hand_ranking, OnePair) and isinstance(heads_up_hand_rankings.second_hand_ranking, OnePair):
            if heads_up_hand_rankings.first_hand_ranking.pair_value > heads_up_hand_rankings.second_hand_ranking.pair_value:
                result = HeadsUpResult.FirstHand
            elif heads_up_hand_rankings.first_hand_ranking.pair_value < heads_up_hand_rankings.second_hand_ranking.pair_value:
                result = HeadsUpResult.SecondHand
            else:
                if heads_up_hand_rankings.first_hand_ranking.first_kicker_value > heads_up_hand_rankings.second_hand_ranking.first_kicker_value:
                    result = HeadsUpResult.FirstHand
                elif heads_up_hand_rankings.first_hand_ranking.first_kicker_value < heads_up_hand_rankings.second_hand_ranking.first_kicker_value:
                    result = HeadsUpResult.SecondHand
                else:
                    if heads_up_hand_rankings.first_hand_ranking.second_kicker_value > heads_up_hand_rankings.second_hand_ranking.second_kicker_value:
                        result = HeadsUpResult.FirstHand
                    elif heads_up_hand_rankings.first_hand_ranking.second_kicker_value < heads_up_hand_rankings.second_hand_ranking.second_kicker_value:
                        result = HeadsUpResult.SecondHand
                    else:
                        if heads_up_hand_rankings.first_hand_ranking.third_kicker_value > heads_up_hand_rankings.second_hand_ranking.third_kicker_value:
                            result = HeadsUpResult.FirstHand
                        elif heads_up_hand_rankings.first_hand_ranking.third_kicker_value < heads_up_hand_rankings.second_hand_ranking.third_kicker_value:
                            result = HeadsUpResult.SecondHand
                        else:
                            result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    def __init__(self):
        HeadsUpEquivalentHandRankingResultCalculatorInterface.__init__(self)


class HighCardsResultCalculator(HeadsUpEquivalentHandRankingResultCalculatorInterface):
    @staticmethod
    def calculate_result(heads_up_hand_rankings):
        assert isinstance(heads_up_hand_rankings, HeadsUpHandRankings)

        if isinstance(heads_up_hand_rankings.first_hand_ranking, HighCard) and isinstance(heads_up_hand_rankings.second_hand_ranking, HighCard):
            if heads_up_hand_rankings.first_hand_ranking.high_card_value > heads_up_hand_rankings.second_hand_ranking.high_card_value:
                result = HeadsUpResult.FirstHand
            elif heads_up_hand_rankings.first_hand_ranking.high_card_value < heads_up_hand_rankings.second_hand_ranking.high_card_value:
                result = HeadsUpResult.SecondHand
            else:
                if heads_up_hand_rankings.first_hand_ranking.first_kicker_value > heads_up_hand_rankings.second_hand_ranking.first_kicker_value:
                    result = HeadsUpResult.FirstHand
                elif heads_up_hand_rankings.first_hand_ranking.first_kicker_value < heads_up_hand_rankings.second_hand_ranking.first_kicker_value:
                    result = HeadsUpResult.SecondHand
                else:
                    if heads_up_hand_rankings.first_hand_ranking.second_kicker_value > heads_up_hand_rankings.second_hand_ranking.second_kicker_value:
                        result = HeadsUpResult.FirstHand
                    elif heads_up_hand_rankings.first_hand_ranking.second_kicker_value < heads_up_hand_rankings.second_hand_ranking.second_kicker_value:
                        result = HeadsUpResult.SecondHand
                    else:
                        if heads_up_hand_rankings.first_hand_ranking.third_kicker_value > heads_up_hand_rankings.second_hand_ranking.third_kicker_value:
                            result = HeadsUpResult.FirstHand
                        elif heads_up_hand_rankings.first_hand_ranking.third_kicker_value < heads_up_hand_rankings.second_hand_ranking.third_kicker_value:
                            result = HeadsUpResult.SecondHand
                        else:
                            if heads_up_hand_rankings.first_hand_ranking.fourth_kicker_value > heads_up_hand_rankings.second_hand_ranking.fourth_kicker_value:
                                result = HeadsUpResult.FirstHand
                            elif heads_up_hand_rankings.first_hand_ranking.fourth_kicker_value < heads_up_hand_rankings.second_hand_ranking.fourth_kicker_value:
                                result = HeadsUpResult.SecondHand
                            else:
                                result = HeadsUpResult.Tie
            return result
        else:
            raise RuntimeError("unexpected hand ranking")

    def __init__(self):
        HeadsUpEquivalentHandRankingResultCalculatorInterface.__init__(self)