from card  import Card
from deck  import Deck
from game  import Game
from field import Field
from tkgui import TkGUI

if __name__ == '__main__':

# a number of test functions
#    myCard = Card(0,0,0,0)
    myDeck  = Deck()
    myField = Field(12)
    myGame  = Game(myDeck,myField)

    myDeck.populateDeck()
#    myDeck.printDeck()

    myDeck.shuffleDeck()
#    myDeck.printDeck()

    for f in range(12):
        myField.addCard( myDeck.drawCard() )

#    myDeck[0]['number'] = 4
#    print(myDeck[0]['number'])
#    print (myDeck[0])
#    print ( len(myDeck[0]) )

#    print ( myGame.isSet( myDeck[0],myDeck[1],myDeck[2] ) )

#    for i in range(75):
#        myDeck.drawCard()
#    myDeck.printDeck()

#    print( myDeck[0] )
#    print( myDeck[1] )

#    print( myGame.makeSet( myDeck[0], myDeck[1] ) )

#    myCard = Card(1,0,0,0)
#    print(myCard)

    myGUI = TkGUI(myGame)
    myGUI.run()
