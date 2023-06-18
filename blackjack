




######
# 👀 #
#####
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()

    def get_value(self):
        if self.rank == "Ace":
            return 11
        elif self.rank in ["Jack", "Queen", "King"]:
            return 10
        else:
            return self.rank

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                # Only create 4 of each card value
                for i in range(4):
                    self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        for card in self.cards:
            value += card.value

        # If the hand contains an Ace and the value is over 21, then the Ace can be worth 1 instead of 11.
        if value > 21 and 1 in [card.value for card in self.cards]:
            value -= 10

        return value

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.dealer_hand = Hand()
        self.player_hand = Hand()

    def start_game(self):
        self.deck.shuffle()
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())

    def hit(self, hand):
        hand.add_card(self.deck.deal())

    def stand(self, hand):
        pass

    def play(self):
        self.start_game()

        while True:
            # The player can hit or stand.
            while True:
                user_input = input("Hit or Stand? ")
                if user_input == "Hit":
                    self.hit(self.player_hand)
                elif user_input == "Stand":
                    break

            # If the player busts, they lose.
            if self.player_hand.get_value() > 21:
                print("You Busted! Dealer Wins!")
                break

            # The dealer will hit until their hand is worth 17 or more.
            while self.dealer_hand.get_value() < 17:
                self.hit(self.dealer_hand)

            # If the dealer busts, the player wins.
            if self.dealer_hand.get_value() > 21:
                print("Dealer Busted! You Win!")
                break

            # Otherwise, the game is a tie.
            if self.player_hand.get_value() == self.dealer_hand.get_value():
                print("Tie Game!")
                break

            # Otherwise, the player wins if their hand is worth more than the dealer's hand.
            if self.player_hand.get_value() > self.dealer_hand.get_value():
                print("You Win!")
                break
            else:
                print("Dealer Wins!")
                break

if __name__ == "__main__":
    game = BlackjackGame()
    game.play()

