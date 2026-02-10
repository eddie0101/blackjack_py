from card import Card
from deck import Deck
from hand import Hand
from player import Player
def main():
    deck = Deck()
    deck.shuffle()
    player = Player("Eddie")
    for _ in range(2):
        dealt_card = deck.deal_card()
        player.recieve_card(dealt_card)
    print(player)

if __name__ == "__main__":
    main()

