# import tkinter
# from tkinter import * #why....? for constants --> cleanup
from .cardcanvas import CardCanvas
from .game import Game
from .deck import Deck
from .field import Field
from .setkaart import SetKaart
from browser import document, html

class BryUI():
    ncols = 4
    nrows = 3

    def __init__(self, game, gui_div_id):
        self.game = game
        self.root = document[gui_div_id]
        # self.root.textContent = "__init__()"
        self.cards = []
        for i in range(self.ncols):
            for j in range(self.nrows):
                self.cards.append( CardCanvas(None, i*self.ncols+j,
                                              "name"+str(i*self.ncols+j),
                                              None ) )
#                print( j, i, " - ", self.cards[-1].number, self.cards[-1] )
                # self.cards[-1].grid(row = j, column = i) => position on screen?
