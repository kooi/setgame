import tkinter
from tkinter import * #ugly, req for geometry manager
from game import Game
import turtle

class TkGUI():

    cw = 56
    ch = 89
    ncols = 4
    nrows = 3

    # make a custom Canvas subclass that implements a
    #  selectedstate -> True|False
    #  selectedObject(s) -> remove all selected objects
    #  associatedcard -> Crad object (can be none for blank card)
    #  default sizex and sizey
    #  a drawcard function that takes (symbol, color, shading, number)

    def __init__(self, game):
        self.game = game
        self.root = tkinter.Tk()
        self.root.title('SET') #get out of settings?
        self.selectedWidgetNumbers = []
        self.selectedWidgetIDs = []

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
                                                     width=100, height=100, # get size from game settings?
                                                     bg="white",
                                                     confine=True,
                                                     name=str(j*self.nrows + i) )
                # if not actually on the field, use grid()?
                self.cardCanvas[j*self.nrows + i].grid(row = i, column = j)
        self.drawField()
        fieldFrame.bind_class("Canvas", "<Button-1>", self.callback)


        sideFrame = tkinter.Frame(self.root)
        sideFrame.pack(side=RIGHT)

        b1 = tkinter.Button(sideFrame, text = "testCB()",    command = self.testCB).pack()
        b2 = tkinter.Button(sideFrame, text = "checkSet()")#,  command = self.checkSet)  # requires 3 selected
        b2.pack()
        b3 = tkinter.Button(sideFrame, text = "makeSet()")#,   command = self.makeSet)   # requires 2 selected
        b3.pack()
        b4 = tkinter.Button(sideFrame, text = "countSets()")#, command = self.countSets)
        b4.pack()
        b5 = tkinter.Button(sideFrame, text = "drawThree()")#, command = self.countSets) # requires available sets to be 0
        b5.pack()
        b6 = tkinter.Button(sideFrame, text = "removeId0fromCanvas0()",    command = self.removeId0fromCanvas0).pack()
#        canvas = tkinter.Canvas(sideFrame,width=200,height=200)
#        canvas.pack()

        #####################

#        t = turtle.RawTurtle(canvas)
#        canvas.create_rectangle(20, 20, 0, 0, fill="red")
#        t.forward(50)

    # leave card selected (draw border on canvas or remove border)
    def doCardClick(self, cardnum):
        #msg = tkinter.messagebox.showinfo("cardnum = ", cardnum)
        try:
            i = self.selectedWidgetNumbers.index(cardnum)
            print( self.cardCanvas[cardnum].delete( self.selectedWidgetIDs[i] ) )
            del self.selectedWidgetNumbers[i]
            del self.selectedWidgetIDs    [i]
        except ValueError:
            self.drawBorder(cardnum)
        print( self.selectedWidgetNumbers, self.selectedWidgetIDs )


    def drawBorder(self, cardnum):
        self.selectedWidgetNumbers.append( cardnum )
        self.selectedWidgetIDs    .append( self.cardCanvas[cardnum]
                                               .create_rectangle(-50, -50,
                                                                  49,  49,
                                                                  outline="blue") )


### Button callbacks ###
    def testCB(self):
        msg = tkinter.messagebox.showinfo( "Hello Python", "Hello World")


    def removeId0fromCanvas0(self):
        print( self.cardCanvas[0].find_all() )
        self.cardCanvas[0].delete(6)


    def callback(self, event):
        print( int(event.widget._name) )
#        print ("clicked at", event.x, event.y)
        self.doCardClick( int(event.widget._name) )


    def drawField(self):
        index = 0
        for c in self.cardCanvas:
            # print(index)
            # check if actually a canvas
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
               + "h:" + str(self.game.field[fieldnumber].shading)
               + "c:" + str(self.game.field[fieldnumber].color)   )
        return None


    def run(self):
        self.root.mainloop()
