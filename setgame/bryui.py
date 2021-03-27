# import tkinter
# from tkinter import * #why....? for constants --> cleanup
from .cardcanvas import CardCanvas
from .game import Game
from .deck import Deck
from .field import Field
from .setkaart import SetKaart
from browser import document, html
from browser.widgets.dialog import InfoDialog


class BryUI():
    ncards = 12
    selectedCardText = None
    autoTest = None
    autoMake = None
    numSets = None
    requiredCardText = None
    requiredCard = None
    cards = []

    def __init__(self, game, gui_div_id):
        self.game = game
        self.root = document[gui_div_id]
        self.getCards()
        # hardcode the buttons for now
        document["button-isset"].bind('click', self.testSet)

    def getCards(self):
        # print(self.game.field.__dict__)
        for i in range(len(self.game.field)):
            self.cards.append(CardCanvas(None, i, "name"+str(i), self.game.field[i]))

    def testSet(self, event):
        sc = [] #selectedcards
        # get selected fieldcanvas
        for cc in self.cards:
            if cc.isSelected and isinstance(cc.setcard, SetKaart):
                sc.append(cc)
        print ( sc )
        if len( sc ) == 3:
            rv = self.game.isSet( sc[0].setcard, sc[1].setcard, sc[2].setcard )
            if rv == True:
                msg = InfoDialog("Set!", "Set!")
                # msg = tkinter.messagebox.showinfo( "Set!", "Set!" )
            else:
                msg = InfoDialog( "Set!", "Geen set :(" )
        else:
            msg = InfoDialog("Selecteer 3", "Selecteer precies 3 kaarten.")
