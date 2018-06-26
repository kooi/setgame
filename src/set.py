from setkaart  import SetKaart
from deck  import Deck
from game  import Game
from field import Field
from tkgui import TkGUI

if __name__ == '__main__':

    myDeck  = Deck()
    myField = Field(12)
    myGame  = Game(myDeck,myField)

    myDeck.populateDeck()
    myDeck.shuffleDeck()

    for f in range(12):
        myField.addCard( myDeck.drawCard() )

    myGUI = TkGUI(myGame)
    myGUI.run()
