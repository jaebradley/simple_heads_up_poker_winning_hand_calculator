from src.model.hand import Hand
from src.model.card import Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace
from src.model.suit import Suit

high_card_hand = Hand(
    [
        Ace(Suit.Spades),
        Two(Suit.Clubs),
        King(Suit.Hearts),
        Queen(Suit.Diamonds),
        Jack(Suit.Hearts)
    ]
)

one_pair_hand = Hand(
    [
        Two(Suit.Clubs),
        Two(Suit.Diamonds),
        Three(Suit.Clubs),
        Five(Suit.Hearts),
        Four(Suit.Diamonds)
    ]
)

two_pair_hand = Hand(
    [
        Two(Suit.Clubs),
        Two(Suit.Diamonds),
        Three(Suit.Clubs),
        Three(Suit.Diamonds),
        Five(Suit.Clubs)
    ]
)

full_house_hand = Hand(
    [
        Two(Suit.Clubs),
        Two(Suit.Diamonds),
        Three(Suit.Clubs),
        Three(Suit.Diamonds),
        Three(Suit.Clubs)
    ]
)

three_of_a_kind_hand = Hand(
    [
        Ace(Suit.Clubs),
        Two(Suit.Diamonds),
        Three(Suit.Clubs),
        Three(Suit.Diamonds),
        Three(Suit.Clubs)
    ]
)

four_of_a_kind_hand = Hand(
    [
        Two(Suit.Clubs),
        Two(Suit.Diamonds),
        Two(Suit.Hearts),
        Two(Suit.Spades),
        Ace(Suit.Spades)
    ]
)

low_straight_hand = Hand(
    [
        Two(Suit.Clubs),
        Three(Suit.Hearts),
        Four(Suit.Spades),
        Five(Suit.Diamonds),
        Ace(Suit.Spades)
    ]
)

high_straight_hand = Hand(
    [
        Jack(Suit.Diamonds),
        King(Suit.Clubs),
        Ten(Suit.Hearts),
        Queen(Suit.Clubs),
        Ace(Suit.Spades)
    ]
)

flush_hand = Hand(
    [
        Two(Suit.Clubs),
        Three(Suit.Clubs),
        Four(Suit.Clubs),
        Jack(Suit.Clubs),
        King(Suit.Clubs)
    ]
)

low_straight_flush_hand = Hand(
    [
        Two(Suit.Clubs),
        Three(Suit.Clubs),
        Four(Suit.Clubs),
        Five(Suit.Clubs),
        Ace(Suit.Clubs)
    ]
)

high_straight_flush_hand = Hand(
    [
        Ace(Suit.Clubs),
        Queen(Suit.Clubs),
        Ten(Suit.Clubs),
        King(Suit.Clubs),
        Jack(Suit.Clubs)
    ]
)