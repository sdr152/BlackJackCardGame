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
        raise NotImplementedError("You must implement get_name() from Player1 or Player2")

    def get_dealt_card(self):
        raise NotImplementedError("You must implement get_dealt_card() from Player1 or Player2")

class Player1(RunPlayerInterface):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0
    
    def get_name(self):
        print(f"Player1 name: {self.name}")

    def get_dealt_card(self, card):
        if len(card) == 3 and "10" in card:
            self.score += 10
        if len(card) == 2 and card[0].isdigit():
            self.score += int(card[0])
        if card[0] in ["K", "Q", "J"]:
            self.score += 10
        if card[0] == "A" and 21-self.score >= 10:
            self.score += 11
        if card[0] == "A" and 21-self.score < 10:
            self.score += 1
        print(f"Player 1 card dealt. {card}, {self.score}")

class Player2(RunPlayerInterface):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0
    
    def get_name(self):
        print(f"Player2 name: {self.name}")
    
    def get_dealt_card(self, card):
        if len(card) == 3 and "10" in card:
            self.score += 10
        if len(card) == 2 and card[0].isdigit():
            self.score += int(card[0])
        if card[0] in ["K", "Q", "J"]:
            self.score += 10
        if card[0] == "A" and 21-self.score >= 10:
            self.score += 11
        if card[0] == "A" and 21-self.score < 10:
            self.score += 1
        print(f"Player 2 card dealt. {card}, {self.score}")


def main():
    D = Deck()
    player1 = Player1("Samson")
    player2 = Player2("Beef")
    D.get_deck()
    
    player1.get_name()
    for i in range(7):
        card = D.deal_card()
        player1.get_dealt_card(card)

        card2 = D.deal_card()
        player2.get_dealt_card(card)

if __name__ == "__main__":
    main()
