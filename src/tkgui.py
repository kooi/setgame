import tkinter
from tkinter import *
from game import Game
import turtle

class TkGUI():

    cw = 56
    ch = 89
    ncols = 4
    nrows = 3

    def __init__(self, game):
        self.game = game
        self.root = tkinter.Tk()
        self.root.title('SET') #get out of settings?

        fieldFrame = tkinter.Frame(self.root)
        fieldFrame.pack(side=LEFT)

#        cardButtons = [None]*20
#        for j in range(3):
#            for i in range(4):
#                cardButtons[j*4 + i] = tkinter.Button(fieldFrame,
#                                                      text = str(j*4+i),
#                                                      command = lambda num=j*4+i: self.doCardClick(num) )
#                cardButtons[j*4 + i].config(height=10, width=10)
#                cardButtons[j*4 + i].grid(row = j, column = i)

        self.cardCanvas = [None]*21 #max 21 cards?
        for i in range(self.nrows):
            for j in range(self.ncols):
                self.cardCanvas[j*self.nrows + i] = tkinter.Canvas(fieldFrame,
                                                     width=100, height=100,
                                                     bg="white",
                                                     confine=True)
                #if not actually on the field, use grid()
                self.cardCanvas[j*self.nrows + i].grid(row = i, column = j)
        self.drawField()

        sideFrame = tkinter.Frame(self.root)
        sideFrame.pack(side=RIGHT)

        b1 = tkinter.Button(sideFrame, text = "testCB()", command = self.testCB)
        b1.pack()
        b2 = tkinter.Button(sideFrame, text = "testCB()", command = self.testCB)
        b2.pack()
        b3 = tkinter.Button(sideFrame, text = "testCB()", command = self.testCB)
        b3.pack()
        b4 = tkinter.Button(sideFrame, text = "testCB()", command = self.testCB)
        b4.pack()
#        canvas = tkinter.Canvas(sideFrame,width=200,height=200)
#        canvas.pack()

        #####################

#        t = turtle.RawTurtle(canvas)
#        canvas.create_rectangle(20, 20, 0, 0, fill="red")
#        t.forward(50)


    def testCB(self):
        msg = tkinter.messagebox.showinfo( "Hello Python", "Hello World")


    def doCardClick(self, cardnum):
        msg = tkinter.messagebox.showinfo("cardnum = ", cardnum)


    def drawField(self):
        index = 0
        for c in self.cardCanvas:
            print(index)
            #check if actually a canvas
            if isinstance(c, Canvas):
                self.drawCard(index)
                index += 1
        # if card is new call drawcard, else leave button as is
        return None


    def drawCard(self, fieldnumber):
        t = turtle.RawTurtle(self.cardCanvas[fieldnumber])
        # DEFAULT: write cardnumber
        # t.write(str(fieldnumber))
        # TODO: get self.game.field[fieldnumber].card
        print( self.game.field[fieldnumber] )
        t.write( "n:" + str(self.game.field[fieldnumber].number)
               + "y:" + str(self.game.field[fieldnumber].symbol)
               + "h:"+ str(self.game.field[fieldnumber].shading)
               + "c:"  + str(self.game.field[fi eldnumber].color)   )
        return None


    def run(self):
        self.root.mainloop()
