from hand import *


if __name__ == "__main__":
    ace = Card("7", "Hearts")
    seven = Card("7","Clubs")
    eight=Card("7","Pica")
    two=Card("7","Diamonds")
    mano = Hand()
    mano + ace
    mano + seven
    mano + eight
    mano + two
    #mano + two
    print(mano)
    print(f"Four of a kind?: {mano.is_four_of_a_kind()}")
