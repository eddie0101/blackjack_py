import os
from deck import Deck
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

    while True:
        print()
        bet_amounts = {}
        for player in players[:-1]:
            print(f"Welcome {player.name}! You have {player.chips} chips to bet with. ")
            print("You can leave the game at any time by entering 'q' when prompted for a bet.")
            bet = input(f"{player.name}, how much would you like to bet? (Enter a number): ")
            if bet.lower() == 'q':
                print(f"{player.name} has left the game.")
                players.remove(player)
                continue
            while not bet.isdigit() or int(bet) <= 0 or int(bet) > player.chips:
                print("Invalid bet. Please enter a positive number that does not exceed your available chips.")
                bet = input(f"{player.name}, how much would you like to bet? (Enter a number): ")
            player.chips -= int(bet)
            print(f"{player.name} has bet {bet} chips. Remaining chips: {player.chips}")
            bet_amounts[player.name] = int(bet)
        for _ in range(2):
            for player in players:
                dealt_card = deck.deal_card()
                player.receive_card(dealt_card)
        
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
                for plr in players:
                    print(plr)
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
                    

        # Determine winner
        # if player busts, dealer wins
        # if dealer busts, player wins
        # if both player and dealer have same hand value, it's a tie
        # if player hand value > dealer hand value, player wins
        # if dealer hand value > player hand value, dealer wins

        print("\nFinal Results:")
        dealer = players[-1]
        for player in players[:-1]:
            if player.hand.get_value() > 21:
                print(f"{player.name} busts! Dealer wins. ") # Player loses bet
            elif dealer.hand.get_value() > 21:
                print(f"{dealer.name} busts! {player.name} wins. ")
                player.chips += bet_amounts[player.name] * 2 # Player wins double the bet
            elif player.hand.get_value() == dealer.hand.get_value():
                print(f"{player.name} and {dealer.name} tie with a hand value of {player.hand.get_value()} points.")
                player.chips += bet_amounts[player.name]  # Return bet to player
            elif player.hand.get_value() > dealer.hand.get_value():
                print(f"{player.name} wins with a hand value of {player.hand.get_value()} points! ")
                player.chips += bet_amounts[player.name] * 2 # Player wins double the bet
            elif player.hand.get_value() == 21:
                print(f"{player.name} wins with a hand value of 21 points! ")
                player.chips += bet_amounts[player.name] * 2.5 # Player wins 2.5 times the bet for Blackjack
            else:
                print(f"{dealer.name} wins over {player.name} with a hand value of {dealer.hand.get_value()} points! ")
                # Player loses bet
        
        print("\nUpdated chip counts:")
        for player in players[:-1]:
            print(f"{player.name}: {player.chips} chips")
    
if __name__ == "__main__":
    main()

