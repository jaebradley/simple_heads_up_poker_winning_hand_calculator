class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        assert 14 > self.value > 1

    def __str__(self):
        return "{0} - {1}".format(self.value, self.suit)


class Two(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 2, suit)


class Three(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 3, suit)


class Four(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 4, suit)


class Five(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 5, suit)


class Six(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 6, suit)


class Seven(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 7, suit)


class Eight(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 8, suit)


class Nine(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 9, suit)


class Ten(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 10, suit)


class Jack(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 11, suit)


class Queen(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 12, suit)


class King(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 13, suit)


class Ace(Card):
    def __str__(self):
        return Card.__str__(self)

    def __init__(self, suit):
        Card.__init__(self, 14, suit)
