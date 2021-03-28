import random
from .setkaart import SetKaart


class Deck():
    """
    Een Deck bestaat uit 81 unique SetKaart-objecten. Als een kaart getrokken
    wordt, wordt deze overgebracht naar het speelveld.
    """

    def __init__(self):
        """
        Normal method does a populate and shuffle.
        """
        self.deck = []


    def populateDeck(self):
        """
        Maakt een nieuw Deck object aan waarin alle mogelijke kaarten voorkomen
        door een loop te maken over de hoeveelheid, kleur, vorm en vulling.
        """

        for hoeveelheid in [1, 2, 3]:
            for kleur in [1, 2, 3]:
                for vorm in [1, 2, 3]:
                    for vulling in [1, 2, 3]:
                        self.addCard( SetKaart(hoeveelheid, kleur, vorm, vulling) )


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
            cardnum = cardnum + 1


    def __getitem__(self, key):
        return self.deck[key]
