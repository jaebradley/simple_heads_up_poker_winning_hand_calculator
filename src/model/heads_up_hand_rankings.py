from src.model.hand_ranking import HandRanking
from src.model.hand_ranking import HighCard, OnePair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush


class HeadsUpHandRankings:
    def __init__(self, first_hand_ranking, second_hand_ranking):

        assert isinstance(first_hand_ranking, HandRanking)
        assert isinstance(second_hand_ranking, HandRanking)

        self.first_hand_ranking = first_hand_ranking
        self.second_hand_ranking = second_hand_ranking

    def are_same_hand_rankings(self):
        if isinstance(self.first_hand_ranking, StraightFlush) and isinstance(self.second_hand_ranking, StraightFlush):
            return True

        elif isinstance(self.first_hand_ranking, FourOfAKind) and isinstance(self.second_hand_ranking, FourOfAKind):
            return True

        elif isinstance(self.first_hand_ranking, FullHouse) and isinstance(self.second_hand_ranking, FullHouse):
            return True

        elif isinstance(self.first_hand_ranking, Flush) and isinstance(self.second_hand_ranking, Flush):
            return True

        elif isinstance(self.first_hand_ranking, Straight) and isinstance(self.second_hand_ranking, Straight):
            return True

        elif isinstance(self.first_hand_ranking, ThreeOfAKind) and isinstance(self.second_hand_ranking, ThreeOfAKind):
            return True

        if isinstance(self.first_hand_ranking, TwoPair) and isinstance(self.second_hand_ranking, TwoPair):
            return True

        if isinstance(self.first_hand_ranking, OnePair) and isinstance(self.second_hand_ranking, OnePair):
            return True

        elif isinstance(self.first_hand_ranking, HighCard) and isinstance(self.second_hand_ranking, HighCard):
            return True

        else:
            return False