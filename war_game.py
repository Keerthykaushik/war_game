from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:

    def __init__(self):
        print("Creating New Ordered Deck")
        self.deck = [(i, j) for i in SUITE for j in RANKS]

    def shuffle(self):
        print("Shuffling")
        shuffle(self.deck)

    def splitting(self):
        return (self.deck[:26], self.deck[26:])


class Hand:

    def __init__(self,cards):
        print("Hand class")
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(self.cards)

    def add(self, added_card):
        self.cards.extend(added_card)

    def remove(self):
        return self.cards.pop(0)


class Player:

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        print("{} has placed: {}".format(self.name, drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards)!=0



print("Welcome to War, let's begin...")

d = Deck()
d.shuffle()
(half1, half2) = d.splitting()

comp = Player("computer", Hand(half1))
player2 = input("What is your name?")
user = Player(player2, Hand(half2))

total_rounds = 0
war_counts = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds+=1
    print("Time for the new round")
    print("Here are the current standings")
    print(user.name+" has the count:{}".format(len(user.hand.cards)))
    print(comp.name + " has the count:{}".format(len(comp.hand.cards)))
    print("play a card")
    print("\n")

    table_cards = []

    c_card = comp.play_card()
    u_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(u_card)

    if c_card[1] == u_card[1]:
        war_counts += 1
        print("WAR!!")
        table_cards.extend(comp.remove_war_cards())
        table_cards.extend(user.remove_war_cards())
        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game Over, Number of rounds:{}".format(total_rounds))
print("A war happened:{} times".format(war_counts))
print("Does the computer still has cards?")
print(str(comp.still_has_cards()))
print("Does the user still has cards?")
print(str(user.still_has_cards()))
