from random import shuffle
class Deck:
    def __init__(self):
        self.get_deck()

    def get_deck(self):
        nums = [str(i) for i in range(2, 11)] + ["A", "K", "Q", "J"]
        syms = ["H", "S", "T", "D"]
        self.deck = [num+sym for sym in syms for num in nums]

    def shuffle_deck(self):
        shuffle(self.deck)
        print(self.deck)
    def make_copy(self):
        deck_copy = self.deck.copy()
        return deck_copy



d = Deck()
d.shuffle_deck()