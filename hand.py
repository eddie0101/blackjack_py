class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)
    
    def get_value(self):
        value = 0
        for card in self.cards:
            if card.rank in ['10', 'Jack', 'Queen', 'King']:
                value += 10
            elif card.rank == 'Ace':
                value += 11
            else:
                value += int(card.rank)
        # Adjust for Aces if value exceeds 21
        if value > 21:
            for card in self.cards:
                if card.rank == 'Ace':
                    value -= 10
                    if value <= 21:
                        break
        return value
    

