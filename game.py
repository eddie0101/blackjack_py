import os
from typing import Dict, List

from deck import Deck
from player import Player


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def _ensure_dealer_is_last(players: List[Player]) -> None:
    if not players:
        return
    if players[-1].name == "Dealer":
        return
    for idx, player in enumerate(players):
        if player.name == "Dealer":
            players[idx], players[-1] = players[-1], players[idx]
            return


def _reset_hands(players: List[Player]) -> None:
    for player in players:
        player.hand.cards = []


def _collect_bets(players: List[Player]) -> Dict[str, int]:
    bet_amounts: Dict[str, int] = {}
    for player in players[:-1]:
        print(f"Welcome {player.name}! You have {player.chips} chips to bet with. ")
        print("You can leave the game at any time by entering 'q' when prompted for a bet.")
        bet = input(f"{player.name}, how much would you like to bet? (Enter a number): ")
        if bet.lower() == "q":
            print(f"{player.name} has left the game.")
            players.remove(player)
            continue
        while not bet.isdigit() or int(bet) <= 0 or int(bet) > player.chips:
            print(
                "Invalid bet. Please enter a positive number that does not exceed your available chips."
            )
            bet = input(f"{player.name}, how much would you like to bet? (Enter a number): ")
        player.chips -= int(bet)
        print(f"{player.name} has bet {bet} chips. Remaining chips: {player.chips}")
        bet_amounts[player.name] = int(bet)
    return bet_amounts


def _deal_initial_cards(deck: Deck, players: List[Player]) -> None:
    for _ in range(2):
        for player in players:
            dealt_card = deck.deal_card()
            if dealt_card is None:
                raise RuntimeError("Deck ran out of cards.")
            player.receive_card(dealt_card)


def _show_table(players: List[Player]) -> None:
    print()
    for player in players:
        print(player)


def _player_turn(deck: Deck, player: Player, players: List[Player]) -> None:
    while True:
        _show_table(players)
        action = input(f"{player.name}, do you want to hit or stand? (h/s): ")
        if action.lower() == "h":
            dealt_card = deck.deal_card()
            if dealt_card is None:
                raise RuntimeError("Deck ran out of cards.")
            player.receive_card(dealt_card)
            print()
            print(player)
            if player.hand.get_value() > 21:
                print(f"{player.name} busts! Dealer wins.")
                break
            if player.hand.get_value() == 21:
                print(f"{player.name} Blackjack! ")
                break
        elif action.lower() == "s":
            print(
                f"{player.name} stands with a hand value of {player.hand.get_value()} points."
            )
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")


def _dealer_turn(deck: Deck, dealer: Player) -> None:
    if dealer.hand.cards:
        dealer.hand.cards[0].hidden = False
    print()
    print(dealer)

    while dealer.hand.get_value() < 17:
        print(f"{dealer.name} hits.")
        dealt_card = deck.deal_card()
        if dealt_card is None:
            raise RuntimeError("Deck ran out of cards.")
        dealer.receive_card(dealt_card)
        print(dealer)


def _is_natural_blackjack(player: Player) -> bool:
    return len(player.hand.cards) == 2 and player.hand.get_value() == 21


def _resolve_round(players: List[Player], bet_amounts: Dict[str, int]) -> None:
    print("\nFinal Results:")
    dealer = players[-1]

    for player in players[:-1]:
        bet = bet_amounts.get(player.name, 0)
        player_value = player.hand.get_value()
        dealer_value = dealer.hand.get_value()

        if player_value > 21:
            print(f"{player.name} busts! Dealer wins. ")
            continue

        if dealer_value > 21:
            print(f"{dealer.name} busts! {player.name} wins. ")
            player.chips += bet * 2
            continue

        if _is_natural_blackjack(player) and dealer_value != 21:
            print(f"{player.name} wins with a hand value of 21 points! ")
            player.chips += (bet * 5) // 2
            continue

        if player_value == dealer_value:
            print(
                f"{player.name} and {dealer.name} tie with a hand value of {player_value} points."
            )
            player.chips += bet
            continue

        if player_value > dealer_value:
            print(f"{player.name} wins with a hand value of {player_value} points! ")
            player.chips += bet * 2
            continue

        print(
            f"{dealer.name} wins over {player.name} with a hand value of {dealer_value} points! "
        )

    print("\nUpdated chip counts:")
    for player in players[:-1]:
        print(f"{player.name}: {player.chips} chips")

# cli - command line interface
def run_cli_game() -> None:
    clear_screen()

    players: List[Player] = [Player("Eddie"), Player("Bob"), Player("Dealer")]
    _ensure_dealer_is_last(players)

    while True:
        if len(players) <= 1:
            print("No players left. Game over.")
            return

        print()
        _reset_hands(players)

        deck = Deck()
        deck.shuffle()

        bet_amounts = _collect_bets(players)
        if len(players) <= 1:
            print("No players left. Game over.")
            return

        _deal_initial_cards(deck, players)

        for player in players:
            if player.name == "Dealer":
                _dealer_turn(deck, player)
                break
            _player_turn(deck, player, players)

        _resolve_round(players, bet_amounts)
