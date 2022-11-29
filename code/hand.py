import copy
from card import *
from myexceptions import *

class Hand:
    def __init__(self):
        self.hand= []
    def add_card(self,card):
        self.hand.append(copy.copy(card))
    def __add__(self,card):
        for a_card in self.hand:
            try:
                if card.get_suit()==a_card.get_suit():
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
    
    def highest_card(self):
        carta = [0,'']
        for i in self.hand:
            if i.rack_util() >= carta[0]:
                carta[0] = i.rack_util()
                carta[1] = i.get_suit()

        dick = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K', 14:'A'}
        return f"{dick[carta[0]]} of {carta[1]}"
    
    
    
    
    
    
    
    
        
    
    
        