from src.model.hand import Hand


class HeadsUp:
    def __init__(self, first_hand, second_hand):

        assert isinstance(first_hand, Hand)
        assert isinstance(second_hand, Hand)

        self.first_hand = first_hand
        self.second_hand = second_hand