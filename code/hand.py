import copy
from myexceptions import *

class Hand:
    def __init__(self):
        self.hand= []
    def add_card(self,card):
        self.hand.append(copy.copy(card))
    def __add__(self,card):
        for a_card in self.hand:
            try:
                if card==a_card:
                    raise CardException("Carta Repetida")
            except CardException as error:
                print(error.message)
                return
        return self.hand.append(copy.copy(card))
    def __repr__(self):
        list_of_cards = ""
        for a_card in self.hand:
            list_of_cards += "{} of {} \n".format(a_card.get_rack(),a_card.get_suit())
        return list_of_cards
    
    def is_four_of_a_kind(self):
        repetitions = self.hand[0].get_rack()
        contador = 0
        for carta in self.hand:
            if carta.get_rack() != repetitions:
                repetitions = carta.get_rack()
            else:
                contador += 1
                if contador == 4:
                    return True, repetitions
        return False