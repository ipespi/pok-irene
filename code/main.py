from card import *
from hand import *


if __name__ == "__main__":
    ace = Card("A", "Hearts")
    seven = Card("7","Hearts")
    eight=Card("8","Hearts")
    two=Card("2","Diamonds")
    mano = Hand()
    mano + ace
    mano + seven
    mano + eight
    mano + two
    mano + two
    print(mano)
    print(f"Four of a kind?: {mano.is_four_of_a_kind()}")
