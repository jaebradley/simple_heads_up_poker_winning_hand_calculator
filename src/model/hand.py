from src.model.card import Card


class Hand:

    def __init__(self, cards):
        self.cards = cards

        assert isinstance(cards, list)
        assert [isinstance(card, Card) for card in cards]

        assert cards.__len__() == 5
