from termcolor import colored
from helpers import create_all_cards, clear
import random

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.deck = create_all_cards()

    def print_cards(self):
        for card in self.cards:
            print(colored(card.get_card_text(), card.color))

    def prompt_card(self, previous_card, game):
        if previous_card.color != "white":
            print("The previous card is: " + colored(previous_card.get_card_text(), previous_card.color))
        card = input("Type a card you want to play: (format: number/name - color). If there's not an usable card, please type draw to get a new card: ")
        while not self.check_card_valid(card, previous_card, game):
            clear()
            print("The previous card is: " + colored(previous_card.get_card_text(), previous_card.color))

            self.print_cards()
            if card == "draw":
                self.draw_card()
            else:
                print("Card not found or not valid!")
            card = input("Type a card you want to play: (format: number/name - color): ")
        return self.remove_card(card)

    def check_card_valid(self, card: str, previous_card, game):
        for c in self.cards:
            if previous_card.color != "white": # need to handle special card, such as everything, stack, etc.
                if str(c) == card and (previous_card.color == c.color or previous_card.number == c.number):
                    if c.special_ability == "reverse":
                        game.reverse()
                    if c.special_ability == "skip":
                        game.skip()
                    return True
            else:
                if str(c) == card:
                    if c.special_ability == "reverse":
                        game.reverse()
                    if c.special_ability == "skip":
                        game.skip()
                    return True
        return False

    def remove_card(self, card: str):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                return c

    def draw_card(self):
        self.cards.append(self.deck[random.randint(0, len(self.deck) - 1)])

