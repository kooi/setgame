import tkinter
from tkinter import *
from cardcanvas import CardCanvas
from game import Game
from deck import Deck
from field import Field
from card import SetCard


class TkGUI():

    ncols = 4
    nrows = 3

    def __init__(self, game):
        self.game = game
        self.root = tkinter.Tk()
        self.root.title('CardCanvasTest') #get out of settings?

        # left: fieldFrame
        self.fieldFrame = tkinter.Frame(self.root)
        self.fieldFrame.pack(side=LEFT)
        self.cards = []
        for i in range(self.ncols):
            for j in range(self.nrows):
                self.cards.append( CardCanvas(self.fieldFrame, i*self.ncols+j,
                                              "name"+str(i*self.ncols+j),
                                              None ) )
                print( j, i, " - ", self.cards[-1].number, self.cards[-1] )
                self.cards[-1].grid(row = j, column = i)
        self.fieldFrame.bind_class("CardCanvas", "<Button-1>", self.canvasCB)
        self.fieldFrame.bind_class("Canvas",     "<Button-1>", self.canvasCB)

    # right: sideFrame
        # debug helpers
        self.sideFrame = tkinter.Frame(self.root)
        self.sideFrame.pack(side=RIGHT)
        self.b1 = tkinter.Button(self.sideFrame, text = "showLabels()", command = self.showLabels).pack()
        self.b2 = tkinter.Button(self.sideFrame, text = "renderAll()" , command = self.renderAll ).pack()
        self.b3 = tkinter.Button(self.sideFrame, text = "clearAll()"  , command = self.clearAll  ).pack()
        self.b4 = tkinter.Button(self.sideFrame, text = "dealCards()" , command = self.dealCards ).pack()

        #game buttons
        self.gb1 = tkinter.Button(self.sideFrame, text = "testSet()"  , command = self.testSet   ).pack()
        self.gb2 = tkinter.Button(self.sideFrame, text = "makeSet()"  , command = self.makeSet   ).pack()
        self.gb3 = tkinter.Button(self.sideFrame, text = "countSets()", command = self.countSets ).pack()
        

## callbacks ##

    def canvasCB(self, event):
#        event.widget.renderCard()
        event.widget.toggleSelect()
#        print( event.widget._name )


    def showLabels(self):
        for c in self.cards:
            c.drawLabel()
#        return None


    def renderAll(self):
        for c in self.cards:
            c.renderCard()


    def clearAll(self):
        for c in self.cards:
            c.clearCanvas()


    def dealCards(self):
        index = 0
        for c in self.game.field:
            self.cards[index].setcard = self.game.field[index]
            index += 1
        self.renderAll()


## game callbacks ##
    # pass 3 cards to game logic, if less than 3 selected
    def testSet(self):
        sc = [] #selectedcards
        # get selected fieldcanvas
        for cc in self.cards:
            if cc.isSelected and isinstance(cc.setcard, SetCard):
                sc.append(cc)
        print ( sc )
        if len( sc ) == 3:
            msg = tkinter.messagebox.showinfo( "", str( self.game.isSet( sc[0].setcard,
                                                                         sc[1].setcard,
                                                                         sc[2].setcard ) ) )
            # call game logic
        else:
            msg = tkinter.messagebox.showinfo("Select 3",
                                              "Please select exactly 3 cards and no empty spaces...")


    # pass 3 cards to game logic, if less than 3 selected
    def makeSet(self):
        sc = [] #selectedcards
        # get selected fieldcanvas
        for cc in self.cards:
            if cc.isSelected and isinstance(cc.setcard, SetCard):
                sc.append(cc)
        print ( sc )
        if len( sc ) == 2:
            r = self.game.makeSet( sc[0].setcard, sc[1].setcard )
            msg = tkinter.messagebox.showinfo( "", str(r['number'])    + ","
                                                   + str(r['symbol'])  + ","
                                                   + str(r['shading']) + ","
                                                   + str(r['color'])         )
            # call game logic
        else:
            msg = tkinter.messagebox.showinfo("Select 2",
                                              "Please select exactly 2 cards and no empty spaces...")


    def countSets(self):
        msg = tkinter.messagebox.showinfo("Sets:",
                                          str(self.game.countSets(self.game.field)) )

###########

    def run(self):
        self.root.mainloop()
