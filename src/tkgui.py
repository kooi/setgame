import tkinter
from tkinter import *  # why....? for constants --> cleanup
from cardcanvas import CardCanvas
from game import Game
from deck import Deck
from field import Field
from setkaart import SetKaart

# TODO: cleanup...
# TODO: extension for more cards than 12...
# TODO: electron/eel backend (can eel do live update of source?)


class TkGUI():

    ncols = 4
    nrows = 3

    def __init__(self, game):
        self.game = game
        self.root = tkinter.Tk()
        self.root.title('SetGame')
        # logo geeft gedonder
        # self.root.wm_iconbitmap(bitmap="@set-logo.xbm")
        # self.root.tk.call('wm','iconphoto',self.root._w,tkinter.PhotoImage(file="res/set-logo.png"))

        # left: fieldFrame
        self.fieldFrame = tkinter.Frame(self.root)
        self.fieldFrame.pack(side=LEFT)
        self.cards = []
        for i in range(self.ncols):
            for j in range(self.nrows):
                self.cards.append(CardCanvas(self.fieldFrame, i * self.ncols + j,
                                             "name" + str(i * self.ncols + j),
                                             None))
#                print( j, i, " - ", self.cards[-1].number, self.cards[-1] )
                self.cards[-1].grid(row=j, column=i)
        self.fieldFrame.bind_class("CardCanvas", "<Button-1>", self.canvasCB)
        self.fieldFrame.bind_class("Canvas",     "<Button-1>", self.canvasCB)

        self.selectedCardText = tkinter.StringVar()
        self.autoTest = tkinter.BooleanVar()
        self.autoMake = tkinter.BooleanVar()
        self.numSets = tkinter.IntVar()
        self.requiredCardText = tkinter.StringVar()
        self.requiredCard = None

    # right: sideFrame
        # debug helpers
        self.sideFrame = tkinter.Frame(self.root)
        self.sideFrame.pack(side=RIGHT, fill=Y)
#        self.b1 = tkinter.Button(self.sideFrame, text = "showLabels()", command = self.showLabels).pack()
#        self.b2 = tkinter.Button(self.sideFrame, text = "renderAll()" , command = self.renderAll ).pack()
#        self.b3 = tkinter.Button(self.sideFrame, text = "clearAll()"  , command = self.clearAll  ).pack()
#        self.b4 = tkinter.Button(self.sideFrame, text = "dealCards()" , command = self.dealCards ).pack()

        # game buttons
        self.sct = tkinter.Label(self.sideFrame, text="Functies:", font='bold').grid(
            row=0, column=0, columnspan=2)
        self.gb1 = tkinter.Button(self.sideFrame, text="isSet()", command=self.testSet).grid(
            row=1, column=0, sticky=E)
        self.cb1 = tkinter.Checkbutton(self.sideFrame, text="auto", variable=self.autoTest,
                                       onvalue=True, offvalue=False).grid(row=1, column=1, sticky=W)
        self.gb2 = tkinter.Button(self.sideFrame, text="maakSet()", command=self.makeSet).grid(
            row=2, column=0, sticky=E)
        self.cb2 = tkinter.Checkbutton(self.sideFrame, text="auto", variable=self.autoMake,
                                       onvalue=True, offvalue=False).grid(row=2, column=1, sticky=W)
#        self.gb3 = tkinter.Button(self.sideFrame, text = "telSets()", command = self.countSets ).grid(row=3,column=0,sticky=E)
        self.sct = tkinter.Label(self.sideFrame, text="Geselecteerde kaarten:", font='bold').grid(
            row=4, column=0, columnspan=2)
        self.l1 = tkinter.Label(self.sideFrame, textvariable=self.selectedCardText).grid(
            row=5, column=0, columnspan=2)
        self.rqc = tkinter.Label(self.sideFrame, text="Benodigde kaart:", font='bold').grid(
            row=6, column=0, columnspan=2)
        #
        self.l2 = tkinter.Label(self.sideFrame, textvariable=self.requiredCardText).grid(
            row=7, column=0, columnspan=2)
        self.pcc = CardCanvas(
            self.sideFrame, 0, "requiredCard", self.requiredCard)
        self.pcc.grid(row=8, column=0, columnspan=2)
        #
        self.nst = tkinter.Label(self.sideFrame, text="Aantal sets:", font='bold').grid(
            row=9, column=0, columnspan=2)
        self.l3 = tkinter.Label(self.sideFrame, textvariable=self.numSets).grid(
            row=10, column=0, columnspan=2)

        self.dealCards()
        self.countSets()


## callbacks ##

    def canvasCB(self, event):
        event.widget.toggleSelect()
        # autocall testSet on selection of 3
        sc = []
        sct = ""
        for cc in self.cards:
            if cc.isSelected and isinstance(cc.setcard, SetKaart):
                sc.append(cc)
                sct += repr(cc.setcard) + '\n'
        self.selectedCardText.set(sct)

        if len(sc) == 2:
            if self.autoMake.get() == True:
                self.makeSet()
        else:
            self.requiredCard = None
            self.pcc.setcard = self.requiredCard
            self.pcc.clearCanvas()
#            self.pcc.renderCard()

        if len(sc) == 3:
            if self.autoTest.get() == True:
                self.testSet()

    def showLabels(self):
        for c in self.cards:
            c.drawLabel()

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
        sc = []  # selectedcards
        # get selected fieldcanvas
        for cc in self.cards:
            if cc.isSelected and isinstance(cc.setcard, SetKaart):
                sc.append(cc)
#        print ( sc )
        if len(sc) == 3:
            rv = self.game.isSet(sc[0].setcard, sc[1].setcard, sc[2].setcard)
            if rv == True:
                msg = tkinter.messagebox.showinfo("Set!", "Set!")
            else:
                msg = tkinter.messagebox.showinfo("Set!", "Geen set :(")
#            msg = tkinter.messagebox.showinfo( "", str( rv ) )
#            if rv == True:
                # remove cards from field and add new
            # call game logic
        else:
            msg = tkinter.messagebox.showinfo("Selecteer 3",
                                              "Selecteer precies 3 kaarten.")

    # pass 3 cards to game logic, if less than 3 selected

    def makeSet(self):
        sc = []  # selectedcards
        # get selected fieldcanvas
        for cc in self.cards:
            if cc.isSelected and isinstance(cc.setcard, SetKaart):
                sc.append(cc)
#        print ( sc )
        if len(sc) == 2:
            r = self.game.maakSet(sc[0].setcard, sc[1].setcard)
            # dit zou het beste gerenderd kunnen worden?
            self.requiredCardText.set(repr(r))
#            msg = tkinter.messagebox.showinfo( "", str(r['hoeveelheid']) + ","
#                                                 + str(r['kleur'])       + ","
#                                                 + str(r['vorm'])        + ","
#                                                 + str(r['vulling'])         )
            self.requiredCard = r
            self.pcc.setcard = self.requiredCard
            self.pcc.clearCanvas()
            self.pcc.renderCard()
            # call game logic
        else:
            msg = tkinter.messagebox.showinfo("Selecteer 2",
                                              "Selecteer precies 2 kaarten.")

    def countSets(self):
        #msg = tkinter.messagebox.showinfo("Sets:",str(self.game.telSets(self.game.field)) )
        self.numSets.set(int(self.game.telSets(self.game.field)))


###########


    def run(self):
        self.root.mainloop()
