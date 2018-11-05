import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_threeOfKind(self):
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[k].get_rank():
                        return True
        return False

    def is_fourOfKind(self):
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    for l in range(k + 1, 5):
                        if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[k].get_rank() == \
                                self.cards[l].get_rank():
                            return True
        return False

    def is_twoPair(self):
        xyz = 0
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    xyz = xyz + 1
        if xyz==2:
            return True
        return False

    def is_Flush(self):
        if self.cards[0].get_suit() == self.cards[1].get_suit() == self.cards[2].get_suit() == self.cards[3].get_suit() == self.cards[4].get_suit():
            return True
        return False

    def is_RoyalFlush(self):
        list1 = []
        for i in range(5):
            list1.append(self.cards[i].get_rank())
        sorted = list1.sort()
        if self.cards[0].get_suit() == self.cards[1].get_suit() == self.cards[2].get_suit() == self.cards[3].get_suit() == self.cards[4].get_suit() and sorted.get_rank() == "10" and sorted.get_rank() == "J" and sorted.get_rank() == "Q" and sorted.get_rank() == "K" and sorted.get_rank() == "A":
            return True
        return False

    def is_fullHouse(self):
        xyz = 0
        boom = 0
        kerfuffle = 0
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    xyz = xyz + 1
        if xyz == 1:
            boom = boom + 1
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[k].get_rank():
                        kerfuffle = kerfuffle + 1
        if kerfuffle == 1:
            boom = boom + 1
        if boom == 2:
            return True
        return False

new_deck = Deck()
new_deck.shuffle()
#print(new_deck)
hand = Hand(new_deck)
#print(hand)
#print(hand.is_pair())
#print(hand.is_threeOfKind())
#print(hand.is_fourOfKind())
for i in range(10000):
    new_deck = Deck()
    new_deck.shuffle()
    hand = Hand(new_deck)
    if hand.is_twoPair() == True:
        print(hand)