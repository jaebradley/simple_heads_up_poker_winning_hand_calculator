from src.model.hand_ranking import HandRanking


class HeadsUpHandRankings:
    def __init__(self, first_hand_ranking, second_hand_ranking):

        assert isinstance(first_hand_ranking, HandRanking)
        assert isinstance(second_hand_ranking, HandRanking)

        self.first_hand_ranking = first_hand_ranking
        self.second_hand_ranking = second_hand_ranking

    def are_same_hand_rankings(self):
        if type(self.first_hand_ranking) == type(self.second_hand_ranking):
            return True
        else:
            return False