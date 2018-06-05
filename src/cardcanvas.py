import tkinter
import turtle
from setkaart import SetKaart


class CardCanvas(tkinter.Canvas):


    def __init__(self, parent, number, name, setcard):
        self.sizex  = 180 #
        self.sizey = 240 #
        self.bgcolor = "white"
        self.selectedColor = "blue"
        self.isSelected = False
        self.selectedTag = "selectedItem"
        self.selectedId = None
        self.name = name
        self.number = number
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
        return self.create_rectangle(-self.sizex/2+1, -self.sizey/2+1,
                                      self.sizex/2-2,  self.sizey/2-2,
                                      width=3, outline=self.selectedColor)


    def drawLabel(self):
        tina = self.myTurtle
        if self.setcard == None:
            tina.write( self.number )
        else:
            tina.write(
                          str(self.setcard.hoeveelheid ) + ","
                        + str(self.setcard.kleur ) + ","
                        + str(self.setcard.vorm) + ","
                        + str(self.setcard.vulling  ) )


    def testDraw(self):
        tina = self.myTurtle
        tina.forward(10)
        tina.right(10)


    def clearCanvas(self):
        tina = self.myTurtle
        tina.clear()


    def tekenOvaal(self, tina, randkleur, vulkleur):
        tina.speed(0)
        tina.pensize(3)
        tina.pencolor(randkleur)
        tina.fillcolor(vulkleur)
        tina.begin_fill()
        tina.forward(30)
        tina.circle(30, 180)
        tina.forward(60)
        tina.circle(30, 180)
        tina.forward(30)
        tina.end_fill()


    def tekenRuit(self, tina, randkleur, vulkleur):
        tina.speed(0)
        tina.pensize(3)
        tina.pencolor(randkleur)
        tina.fillcolor(vulkleur)
        tina.begin_fill()
        tina.left(90)
        tina.forward(15)
        tina.right(90)
        tina.forward(60)
        tina.left(150)
        tina.forward(60)
        tina.left(60)
        tina.forward(60)
        tina.left(120)
        tina.forward(60)
        tina.left(60)
        tina.forward(60)
        tina.right(30)
        tina.end_fill()


    def tekenGolf(self, tina, randkleur, vulkleur):
        tina.speed(0)
        tina.pensize(3)
        tina.pencolor(randkleur)
        tina.fillcolor(vulkleur)
        tina.begin_fill()
        tina.circle(45, 90)
        tina.circle(15, 90)
        tina.forward(30)
        tina.circle(45, 90)
        tina.circle(15, 90)
        tina.forward(30)
        tina.end_fill()


    def renderCard(self):
        """
        Laat tina de correcte tekening maken op de kaart. Maakt gebruik van
        de hulpfuncties tekenOvaal(), tekenRuit(), tekenGolf()
        """
        randkleuren = ['red', 'purple', 'green']
        vulkleuren = [  ['red',    'pink',          'white'],
                        ['purple', 'MediumPurple1', 'white'],
                        ['green',  'light green',   'white']  ]
        xy = []
        tina = self.myTurtle
        if self.setcard == None:
            self.drawLabel()
        else:
            if self.setcard.hoeveelheid == 3:
                xy = [ [0, -105],
                       [0, -30],
                       [0,  45]  ]
            elif self.setcard.hoeveelheid == 2:
                xy = [ [0, -60],
                       [0, 30]  ]
            elif self.setcard.hoeveelheid == 1:
                xy = [ [0, -30] ]

            for pos in xy:
                tina.goto(pos[0],pos[1])

                if self.setcard.vorm == 1: #ovaal
                        self.tekenOvaal(tina,
                                        randkleuren[self.setcard.kleur-1],
                                        vulkleuren[self.setcard.kleur-1][self.setcard.vulling-1] )
                elif self.setcard.vorm == 2: #ruit
                        self.tekenRuit(tina,
                                        randkleuren[self.setcard.kleur-1],
                                        vulkleuren[self.setcard.kleur-1][self.setcard.vulling-1] )
                elif self.setcard.vorm == 3: #golf
                        self.tekenGolf(tina,
                                        randkleuren[self.setcard.kleur-1],
                                        vulkleuren[self.setcard.kleur-1][self.setcard.vulling-1] )
