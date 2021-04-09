from .cardcanvas import CardCanvas
from .game import Game
from .deck import Deck
from .field import Field
from .setkaart import SetKaart
from browser import document, html, alert, bind


class BryUI():
    ncards = 12
    autoTest = None
    autoMake = None
    numSets = None
    requiredCardText = None
    requiredCard = None
    cards = []
    selectedCards = []

    def __init__(self, game, gui_div_id, code_div_id):
        self.game = game
        self.root = document[gui_div_id]
        self.code = document[code_div_id]
        self.getCards()

        document["button-countset"].bind("click", self.countSets)
        document["button-isset"].bind('click', self.testSet)
        document["canvas-field"].bind('click', self.updateSelectedCards)

    def countSets(self, event):
        document["number-of-sets"].html = self.game.telSets(self.game.field)

    def getCards(self):
        self.cards = []
        for i in range(len(self.game.field)):
            self.cards.append(CardCanvas(
                None, i, "name"+str(i), self.game.field[i]))

    def testSet(self, event):
        sc = self.selectedCards
        if len(sc) == 3:
            rv = self.game.isSet(sc[0].setcard, sc[1].setcard, sc[2].setcard)
            if rv == True:
                msg = alert("Set!")
            else:
                msg = alert("Geen set :(")
        else:
            msg = alert("Selecteer precies 3 kaarten.")

    def updateSelectedCards(self, event):
        self.selectedCards = []
        for cc in self.cards:
            if cc.isSelected and isinstance(cc.setcard, SetKaart):
                self.selectedCards.append(cc)
        self.updateSelectedCardsText()

    def updateSelectedCardsText(self):
        sct = ""
        for card in self.selectedCards:
            sct += repr(card.setcard)+'<br>'
        document["selected_cards"].html = sct
