from card import Card
from deck import Deck
from hand import Hand
from player import Player
def main():
    deck = Deck()
    deck.shuffle()
    player1 = Player("Eddie")
    player2 = Player("Dealer")
    for _ in range(2):
        dealt_card = deck.deal_card()
        player1.recieve_card(dealt_card)
        dealt_card = deck.deal_card()
        player2.recieve_card(dealt_card)
    print(player1)
    print(player2)

if __name__ == "__main__":
    main()

