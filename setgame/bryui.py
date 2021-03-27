# import tkinter
# from tkinter import * #why....? for constants --> cleanup
from .cardcanvas import CardCanvas
from .game import Game
from .deck import Deck
from .field import Field
from .setkaart import SetKaart
from browser import document, html


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
        # self.root.textContent = "__init__()"
        # self.cards = []
        # for i in range(self.ncards):
        #         print( j, i, " - ", self.cards[-1].number, self.cards[-1] )
        #         self.cards[-1].grid(row = j, column = i) => position on screen?
        self.getCards()
        # self.renderAll()
        # self.countSets()

    def getCards(self):
        print(self.game.field.__dict__)
        for i in range(len(self.game.field)):
            self.cards.append(CardCanvas(None, i, "name"+str(i), self.game.field[i]))
            # timer.set_timeout(self.print_debug, 1000)
            # print(self.game.field[i])

    # def print_debug(self):
        # print(self.__dict__)

    # def renderAll(self):
    #     for c in self.cards:
    #         print(c.__dict__)
    #         c.renderCard()
    #         c.testDraw()

    # temp

    # def render(self):
    #     for card in self.cards:
    #         print(card)
    #         card.testDraw()
        # print(self.cards)
        # self.cards[0].testDraw()
        # self.cards[1].testDraw()
