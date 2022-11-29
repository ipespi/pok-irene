from functools import total_ordering

@total_ordering
class Card:
    def __init__(self,rack,suit):
        self.suit=suit
        datos_rack = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14, 'j':11, 'q':12, 'k':13, 'a':14}
        self.rack = datos_rack[rack]
        
  
        
    
    def get_suit(self):
        return self.suit
    
    def get_rack(self):
        ingles_esp = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K', 14:'A'}
        return ingles_esp[self.rack]
    
    def rack_util(self):
        return self.rack
    
    
    def __eq__ ( self,other):
        return self.rack==other.rack
    def __lt__ ( self,other):
        return self.rack<other.rack
    def __ge__(self, other):
        return self.rack>=other.rack