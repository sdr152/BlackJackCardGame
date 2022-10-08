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

class Player:
    def __init__(self, name):
        self.name = name
    
    def get_dealt_card(self):
        raise NotImplementedError("You must implement get_dealt_card() from Player1 or Player2")

class Player1(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def get_dealt_card(self):
        print("Player 1 card dealt")

class Player2(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def get_dealt_card(self):
        print("Player 2 card dealt.")


d = Deck()
print(d.get_deck())
d.get_length()
d.shuffle_deck()
print(d.deal_card())
d.get_length()
print(d.deal_card())
d.get_length()

print('--------')
d2 = Deck()
print(d2.get_deck())
d2.get_length()