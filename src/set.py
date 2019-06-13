"""
Tkinter versie van het spel Set.
"""

from setkaart import SetKaart
from deck import Deck
from game import Game
from field import Field
from tkgui import TkGUI

# importeer hier de gewijzigde versies van game.isSet() en game.maakSet()
# uit game_patch.py
# comment deze weg om de originele versie te gebruiken
import game_patch

if __name__ == '__main__':

    myDeck = Deck()
    myField = Field(12)
    myGame = Game(myDeck, myField)

    myDeck.populateDeck()
    myDeck.shuffleDeck()

    for f in range(12):
        myField.addCard(myDeck.drawCard())

    # tkinter version
    myGUI = TkGUI(myGame)
    myGUI.run()

    # experimental: pysimplegui
