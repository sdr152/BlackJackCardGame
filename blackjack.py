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

    run = True
    while run:
        bet = float(input("How much do you want to bet?  "))
        deck = Deck()
        deck.shuffle_deck()
        player1 = Player1("Samuel")
        dealer = Dealer("Dealer")

        first_hand1 = deck.give_first_two_cards()
        first_hand2 = deck.give_first_two_cards()
        
        player1.get_first_hand(first_hand1)
        dealer.get_first_hand(first_hand2)
        
        player1_score = 0
        for cd in player1.hand:
            v = add_score(cd, player1_score)
            player1_score += v
        dealer_score = add_score(first_hand2[0], 0)
        winner = None
        
        print("------ PLAYER'S TURN! ------\n")
        while True:
            print("Player1 hand: ", player1.hand, "Score Player1: ", player1_score)
            print("Dealer hand: ", dealer.hand, "Score Dealer: ", dealer_score, "\n") 
            
            if player1_score > 21:
                winner = dealer.name
                break

            q = input("Do you want to hit a new card? ").lower()
            if q == 'no' or q == 'n':
                print("You decided to stay!\n")
                break
            
            card = deck.deal_card()
            player1.update_hand(card)
            player1_score += add_score(card, player1_score)

        print("------ DEALER'S TURN ------\n")
        dealer_score += add_score(first_hand2[1], dealer_score)
        while winner==None:
            if dealer_score > 21:
                winner = player1.name
                break
            
            if dealer_score >= 17:
                print("Dealer decides to stay\n")
                break
            
            card = deck.deal_card()
            dealer.update_hand(card)
            dealer_score += add_score(card, dealer_score)
            print("Player1 hand: ", player1.hand, "Score Player1: ", player1_score)
            print("Dealer hand: ", dealer.hand, "Score Dealer: ", dealer_score, "\n") 

        winner, vegas_savings, vault = get_winner(winner, player1, dealer, player1_score, dealer_score, vegas_savings, bet, vault)
        print("WINNER:  ", winner)
        print("Savings: ", vegas_savings)
        print("Casino Vault:  ", vault) 

        play = input("Do you want to bet again?  ").lower()
        run = play=='y' or play=='yes'

if __name__ == "__main__":
    main()
