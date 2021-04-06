"""
Brython versie van het spel Set.
"""

from setgame.setkaart import SetKaart
from setgame.deck import Deck
from setgame.game import Game
from setgame.field import Field
from setgame.bryui import BryUI

# importeer hier de gewijzigde versies van game.isSet() en game.maakSet()
# uit game_patch.py comment deze weg om de originele versie te gebruiken
# import game_patch

if __name__ == '__main__':

    myDeck = Deck()
    myField = Field(12)
    myGame = Game(myDeck, myField)

    myDeck.populateDeck()
    myDeck.shuffleDeck()

    for f in range(12):
        myField.addCard(myDeck.drawCard())

    # brython version
    myGUI = BryUI(myGame, 'setgui', 'ide')

    # experimental: CodeSkulptor3/simplegui
    # experimental: CodeSkulptor3/custom-gui-toolkit

