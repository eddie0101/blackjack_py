class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hidden = False

    def __str__(self):
        if self.hidden:
            return "[ ? ]"
        return f"[ {self.rank} of {self.suit} ]"