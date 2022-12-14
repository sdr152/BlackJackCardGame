from random import shuffle
class Deck:
    cards = [str(i) for i in range(2, 10)] + ["A", "T", "Q", "J", "K"]
    suits = ["D", "H", "C", "S"]

    def __init__(self):
        self.deck = [card+suit for suit in Deck.suits for card in Deck.cards]

    def get_deck(self):
        return self.deck

    def shuffle_deck(self):
        shuffle(self.deck)
    
    def make_copy(self):
        deck_copy = self.deck.copy()
        return deck_copy
    
    def get_length(self):
        print(len(self.deck))
    
    def give_first_two_cards(self):
        return [self.deck.pop(0) for i in range(2)]

    def deal_card(self):
        dealt_card = self.deck.pop(0)
        return dealt_card

class RunPlayerInterface:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def get_name(self):
        raise NotImplementedError("You must implement get_name() from Player1 or Dealer.")

    def get_first_hand(self):
        raise NotImplementedError("You must implement get_first_hand() from Player1 or Dealer.")

    def update_hand(self):
        raise NotImplementedError("You must implement update_hand() from Player1 or Dealer.")

class Player1(RunPlayerInterface):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0
        self.hand = []
    
    def get_name(self):
        print(f"Player1 name: {self.name}")

    def get_first_hand(self, list):
        for card in list:
            self.hand.append(card)

    def update_hand(self, card):
        self.hand.append(card)

class Dealer(RunPlayerInterface):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0
        self.hand = []
    
    def get_name(self):
        print(f"Dealer name: {self.name}")
    
    def get_first_hand(self, list):
        for card in list:
            self.hand.append(card)
    
    def update_hand(self, card):
        self.hand.append(card)
        
def get_value(card, total_score):
    if len(card) == 2 and card[0].isdigit():
        value = int(card[0])
    if card[0] in ["K", "Q", "J", "T"]:
        value = 10
    if card[0] == "A" and 21-total_score >= 10:
        value = 11
    if card[0] == "A" and 21-total_score < 10:
        value = 1
    return value

def get_winner(winner, player1, dealer, player1_score, dealer_score, vegas_savings, bet, vault):
    if winner == None:
        if player1_score > dealer_score:
            winner = player1.name
            vault -= 2*bet
            vegas_savings += 2*bet
        elif player1_score < dealer_score:
            winner = dealer.name
            vegas_savings -= bet
            vault += bet
        else:
            winner = "NO WINNER"
    else:
        if winner == player1.name:
            vault -= 2*bet
            vegas_savings += 2*bet
        elif winner == dealer.name:
            vegas_savings -= bet
            vault += bet
        else:
            winner = "NO WINNER"
    return winner, vegas_savings, vault

def main():
    print("*** WELCOME TO COCO BONGO CASINO! ***\n")
    vegas_savings = 5000
    vault = 0
    print("Available cash: ", vegas_savings)
    print("Casino Vault:   ", vault)

    run = True
    while run:
        #Initialize deck.
        deck = Deck()
        deck.shuffle_deck()

        #Initialize player and dealer.
        player1 = Player1("Samuel")
        dealer = Dealer("Dealer")
        
        # How much does the player want to bet?
        bet = float(input("How much do you want to bet?  "))
        
        # Get first hands of two cards to player and dealer.
        first_hand1 = deck.give_first_two_cards()
        first_hand2 = deck.give_first_two_cards()
        player1.get_first_hand(first_hand1)
        dealer.get_first_hand(first_hand2)
        
        # Update score for the player and partial score for the dealer.
        player1_score = 0
        for cd in player1.hand:
            v = get_value(cd, player1_score)
            player1_score += v
        dealer_score = get_value(first_hand2[0], 0)
        winner = None
        
        print("------ PLAYER'S TURN! ------\n")
        print("Dealer hand: ", dealer.hand[0], "Score Dealer: ", dealer_score, "\n")
        while True:
            print("Player1 hand: ", player1.hand, "Score Player1: ", player1_score)
            
            # Check whether the player's score is over 21 or not.
            if player1_score > 21:
                winner = dealer.name
                break
            
            # Ask the player if he wants to hit a new card.
            q = input("Do you want to hit a new card? ").lower()
            if q == 'no' or q == 'n':
                print("You decided to stay!\n")
                break
            card = deck.deal_card()
            player1.update_hand(card)
            
            # Get value of the card and update score.
            player1_score += get_value(card, player1_score)

        print("------ DEALER'S TURN ------\n")
        dealer_score += get_value(first_hand2[1], dealer_score)
        
        
        while winner==None:
            # If there is still no winner, check wether the dealer's score is over 21 or not.
            if dealer_score > 21:
                winner = player1.name
                break
            
            # Check whether to hit or stay.
            if dealer_score >= 17:
                print("Dealer decides to stay\n")
                break
            
            # Dealer hit new card and updates hand.
            card = deck.deal_card()
            dealer.update_hand(card)

            # Dealer get value from the card and updates score.
            dealer_score += get_value(card, dealer_score)
        
            print("Dealer hand: ", dealer.hand, "Score Dealer: ", dealer_score, "\n") 

        winner, vegas_savings, vault = get_winner(winner, player1, dealer, player1_score, dealer_score, vegas_savings, bet, vault)
        print("Player's hand:   ", player1.hand)
        print("Player's score:  ", player1_score)
        print("Dealer's hand:   ", dealer.hand)
        print("Dealers' score:  ", dealer_score)
        print("WINNER:          ", winner)
        print("Savings:         ", vegas_savings)
        print("Casino Vault:    ", vault) 

        play = input("Do you want to bet again?  ").lower()
        run = play=='y' or play=='yes'

if __name__ == "__main__":
    main()
