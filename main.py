import os
from card import Card
from deck import Deck
from hand import Hand
from player import Player
def main():

    os.system('cls')

    deck = Deck()
    deck.shuffle()
    players = []
    players.append(Player("Eddie"))
    players.append(Player("Bob"))
    players.append(Player("Dealer"))

    # swap dealer with last player if dealer is not last
    if players[-1].name != "Dealer":
        players[0], players[-1] = players[-1], players[0]

    for _ in range(2):
        for player in players:
            dealt_card = deck.deal_card()
            player.receive_card(dealt_card)
    
    print()
    for player in players:
        print(player)
    
    for player in players:
        if player.name == "Dealer":
            player.hand.cards[0].hidden = False
            print()
            print(player)
            while player.hand.get_value() < 17:
                print(f"{player.name} hits.")
                dealt_card = deck.deal_card()
                player.receive_card(dealt_card)
                print(player)
            break
        # Player's turn
        while True:
            print()
            action = input(f"{player.name}, do you want to hit or stand? (h/s): ")
            if action.lower() == 'h':
                dealt_card = deck.deal_card()
                player.receive_card(dealt_card)
                print()
                print(player)
                if player.hand.get_value() > 21:
                    print(f"{player.name} busts! Dealer wins.")
                    break
                elif player.hand.get_value() == 21:
                    print(f"{player.name} Blackjack! ")
                    break
            elif action.lower() == 's':
                print(f"{player.name} stands with a hand value of {player.hand.get_value()} points.")
                break
            else:
                print("Invalid input. Please enter 'h' to hit or 's' to stand.")
                
if __name__ == "__main__":
    main()

