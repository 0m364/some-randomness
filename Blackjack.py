import random

class Card:
    """
    Represents a card in the deck.
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()

    def get_value(self):
        """
        Gets the card's value.
        """
        if self.rank == "Ace":
            return 11
        elif self.rank in ["Jack", "Queen", "King"]:
            return 10
        else:
            return int(self.rank)

class Deck:
    """
    Represents a deck of cards.
    """
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ["Hearts", "Diamonds", "Spades", "Clubs"] 
                      for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]*4]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    """
    Represents a player's hand.
    """
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        hand_value = sum(card.value for card in self.cards)
        # Adjust for Ace
        aces = [card for card in self.cards if card.rank == "Ace"]
        while hand_value > 21 and aces:
            hand_value -= 10
            aces.pop()
        return hand_value

class BlackjackGame:
    """
    Represents the game of blackjack.
    """
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

    def play(self):
        self.start_game()
        while True:
            print(f"\nYour hand: {', '.join(card.rank for card in self.player_hand.cards)}")
            action = input("Would you like to hit or stand? ").lower()
            while action not in ['hit', 'stand']:
                action = input("Invalid input. Please type 'hit' or 'stand'. ").lower()

            if action == 'hit':
                self.hit(self.player_hand)
                if self.player_hand.get_value() > 21:
                    print("You Busted! Dealer Wins!")
                    break
            else:
                while self.dealer_hand.get_value() < 17:
                    self.hit(self.dealer_hand)
                if self.dealer_hand.get_value() > 21:
                    print("Dealer Busted! You Win!")
                    break
                elif self.player_hand.get_value() == self.dealer_hand.get_value():
                    print("It's a tie!")
                    break
                elif self.player_hand.get_value() > self.dealer_hand.get_value():
                    print("You win!")
                    break
                else:
                    print("Dealer Wins!")
                    break

if __name__ == "__main__":
    while True:
        game = BlackjackGame()
        game.play()
        replay = input("Would you like to play again? (Y/N) ").lower()
        if replay != 'y':
            break
