import tkinter
import turtle
from setkaart import SetKaart


class CardCanvas(tkinter.Canvas):


    def __init__(self, parent, number, name, setcard):
        self.sizex  = 100 #
        self.sizey = 150 #
        self.bgcolor = "white" #doesnt work?
        self.selectedColor = "green"
        self.isSelected = False
        self.selectedTag = "selectedItem"
        self.selectedId = None
        self.name = name #required?
        self.number = number #required?
        self.setcard = setcard
        super().__init__(parent, width=self.sizex, height=self.sizey, bg=self.bgcolor, confine=True, name=name)
        self.myTurtle = turtle.RawTurtle(self)


    def toggleSelect(self):
        if self.isSelected == True:
            print( self.delete( self.selectedId ) )
            self.isSelected = False
        else: # self.isSelected == False:
            self.selectedId = self.drawBorder()
            print(self.selectedId)
            self.isSelected = True


    def drawBorder(self):
        return self.create_rectangle(-50, -50, 49,  49, outline=self.selectedColor)


    def drawLabel(self):
        tina = self.myTurtle
        if self.setcard == None:
            tina.write( self.number )
        else:
            tina.write(
                          str(self.setcard.number ) + ","
                        + str(self.setcard.symbol ) + ","
                        + str(self.setcard.shading) + ","
                        + str(self.setcard.color  ) )


    def testDraw(self):
        tina = self.myTurtle
        tina.forward(10)
        tina.right(10)


    def clearCanvas(self):
        tina = self.myTurtle
        tina.clear()


    def tekenOvaal(self, tina, kleur):
        tina


    def renderCard(self):
        """
        Laat tina de correcte tekening maken op de kaart. Maakt gebruik van
        de hulpfuncties tekenOvaal, tekenRuit, tekenGolf,
        """
        tina = self.myTurtle
        if self.setcard:
            tina.write(
                          str(self.setcard.hoeveelheid ) + ","
                        + str(self.setcard.kleur       ) + ","
                        + str(self.setcard.vorm        ) + ","
                        + str(self.setcard.vulling     ) )
