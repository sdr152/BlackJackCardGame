from random import shuffle
class Deck:
    def __init__(self):
        self.cards = [str(i) for i in range(2, 11)] + ["A", "K", "Q", "J"]
        self.suits = ["H", "S", "T", "D"]
        self.deck = [card+suit for suit in self.suits for card in self.cards]

    def get_deck(self):
        return self.deck

    def shuffle_deck(self):
        shuffle(self.deck)
        print(self.deck)
    
    def make_copy(self):
        deck_copy = self.deck.copy()
        return deck_copy
    
    def get_length(self):
        print(len(self.deck))
    
    def deal_card(self):
        dealt_card = self.deck.pop(0)
        return dealt_card

class RunPlayerInterface:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def get_name(self):
        raise NotImplementedError("You must implement get_name() from Player1 or Dealer")

    def update_hand(self):
        raise NotImplementedError("You must implement update_hand() from Player1 or Dealer")

class Player1(RunPlayerInterface):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0
        self.hand = []
    
    def get_name(self):
        print(f"Player1 name: {self.name}")

    def update_hand(self, card):
        self.hand.append(card)

class Dealer(RunPlayerInterface):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0
        self.hand = []
    
    def get_name(self):
        print(f"Dealer name: {self.name}")
    
    def update_hand(self, card):
        self.hand.append(card)
        
    
def add_score(card, total_score):
    if len(card) == 3 and "10" in card:
        value = 10
    if len(card) == 2 and card[0].isdigit():
        value = int(card[0])
    if card[0] in ["K", "Q", "J"]:
        value = 10
    if card[0] == "A" and 21-total_score >= 10:
        value = 11
    if card[0] == "A" and 21-total_score < 10:
        value = 1
    #self.score += value
    return value
    #print(f"Dealer card dealt. {self.hand}, {card}, {self.score}")


def main():
    D = Deck()
    player1 = Player1("Samson")
    dealer = Dealer("Beef Dealer")
    
    player1_score = 0
    dealer_score = 0
    n = 0
    winner = None
    while player1_score < 21 and dealer_score < 21:
        while True:
            x = input("Do you want to deal a new card? ")
            if x == 'yes' or x == 'y':        
                card = D.deal_card()
                player1.update_hand(card)
                player1_score += add_score(card, player1_score)
                break

        while True:
            y = input("Do you want to deal a new card? ")
            if y == "yes" or y == "y":        
                card2 = D.deal_card()
                dealer.update_hand(card2)
                dealer_score += add_score(card2, dealer_score)
                break
       
        n += 1

        if n <= 1:
            continue
        print("Player1 hand: ", player1.hand, "Score Player1: ", player1_score)
        print("Dealer hand: ", dealer.hand, "Score Dealer: ", dealer_score) 
        if player1_score >= 21 or dealer_score >= 21:
            break
        ans = input("Do you wish to pull a new card?  ").lower()
        run = ans == "y" or ans == "yes"
    
    winner = player1.name if player1_score > dealer_score else dealer.name
    print(f'Current winner:  {winner}') 


if __name__ == "__main__":
    main()
