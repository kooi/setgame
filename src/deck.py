

import random
from card import Card

class Deck():
    """
    A Deck consists of 81 unique Card objects. When a card is drawn it should be
    passed to the PlayingField and is removed from the Deck.
    """

    #number 0, 1, 2


    def __init__(self):
        """
        Normal method does a populate and shuffle.
        """
        self.deck = []


    def populateDeck(self):
        """
        Normal populateDeck makes a full sorted Deck according to
        number < symbol < shading < color
        """

        #this way explicitly defines the iteration...not pretty
        for num in [0,1,2]:
            for sym in [0,1,2]:
                for sha in [0,1,2]:
                    for col in [0,1,2]:
                        self.addCard( Card(num,sym,sha,col) )
#                        print('added card')
#                        self.deck.append( Card(num,sym,sha,col) )


    def shuffleDeck(self):
        random.shuffle(self.deck)


    def addCard(self, card):
        self.deck.append(card)


    def drawCard(self):
        return self.deck.pop()


    def printDeck(self):
        """
        Prints the remaining cards of the Deck in order (using int print)
        """
        cardnum = 1
        for card in self.deck:
            print (card)
#            print(cardnum, ':', card)
            cardnum = cardnum + 1


    def __getitem__(self, key):
        return self.deck[key]
