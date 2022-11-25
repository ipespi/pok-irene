from functools import total_ordering

@total_ordering
class Card:
    def __init__(self,rack,suit):
        self.suit=suit
        if rack == "A":
            self.rack= "Z"
        else:
            self.rack=rack
    def get_suit(self):
        return self.suit
    def get_rack(self):
        if self.rack=="Z":
            return "A"
        else:
            return self.rack
    def __eq__ ( self,other):
        return self.rack==other.rack
    def __lt__ ( self,other):
        return self.rack<other.rack