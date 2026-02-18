from hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = 1000  # Starting chips for betting
    
    def receive_card(self, card):
        if self.name == "Dealer" and len(self.hand.cards) == 0:
            card.hidden = True
        self.hand.add_card(card)
    
    def __str__(self):
        if len(self.hand.cards) > 0 and self.hand.cards[0].hidden == True:
            return f"{self.name}'s hand: {self.hand} (Value: ?)"
        return f"{self.name}'s hand: {self.hand} (Value: {self.hand.get_value()})"
    
    def ask_for_card(self):
        response = input(f"{self.name}, do you want another card? (y/n): ")
        return response.lower() == 'y'
    

    