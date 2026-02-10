from hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
    
    def recieve_card(self, card):
        self.hand.add_card(card)
    
    def __str__(self):
        return f"{self.name}'s hand: {self.hand} (Value: {self.hand.get_value()})"
    