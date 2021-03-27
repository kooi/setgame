import brython_turtle as turtle
from .setkaart import SetKaart
from browser import document, html, timer


class CardCanvas():
    """
    HTML Canvas for rendering set cards using python turtle.
    """

    def __init__(self, parent, number, name, setcard):
        self.sizex = 180
        self.sizey = 240
        self.bgcolor = "white"
        self.selectedColor = "blue"
        self.isSelected = False
        self.selectedTag = "selectedItem"
        self.selectedId = None
        self.name = name
        self.number = number
        self.setcard = setcard
        self.element_id = "canvas"+str(self.number)
        self.initTurtleCanvas()
        # timer.set_timeout(self.renderCard, 1000)
        self.renderCard()
        # self.testDraw()
        # timer.set_timeout(turtle.done, 50)
        turtle.done()
        # print("CardCanvas.__init__() completed")
        document[self.element_id].bind('click', self.toggleSelect)

    def initTurtleCanvas(self):
        turtle.set_defaults(
            canvwidth=self.sizex,
            canvheight=self.sizey,
            pencolor="black",
            fillcolor="pink",
            turtle_canvas_wrapper=document[self.element_id]
        )
        self.myTurtle = turtle.Turtle()
        self.myTurtle.shape("turtle")
        self.myTurtle.speed(1)
        self.myTurtle.showturtle()

    def toggleSelect(self, event):
        print('clicked', self.element_id)
        if self.isSelected == True:
            self.isSelected = False
            document[self.element_id].attrs['class'] = 'cardcanvas'
        else:  # self.isSelected == False:
            self.isSelected = True
            document[self.element_id].attrs['class'] = 'cardcanvas selected'

    # def drawLabel(self):
    #     tina = self.myTurtle
    #     if self.setcard == None:
    #         tina.write(self.number)
    #     else:
    #         tina.write(
    #             str(self.setcard.hoeveelheid) + ","
    #             + str(self.setcard.kleur) + ","
    #             + str(self.setcard.vorm) + ","
    #             + str(self.setcard.vulling))

    # def testDraw(self):
    #     turtle.set_defaults(
    #         canvwidth=self.sizex,
    #         canvheight=self.sizey,
    #         pencolor="black",
    #         fillcolor="pink",
    #         turtle_canvas_wrapper=document["canvas"+str(self.number)]
    #     )
    #     self.myTurtle = turtle.Turtle()
    #     self.myTurtle.shape("turtle")
    #     self.myTurtle.speed(0)
    #     tina = self.myTurtle
    #     tina.fillcolor("green")
    #     tina.forward(10)
    #     tina.right(10)
    #     turtle.done()
    #     print(self.myTurtle)

    # def clearCanvas(self):
    #     tina = self.myTurtle
    #     tina.clear()

    def tekenOvaal(self, tina, randkleur, vulkleur):
        tina.speed(0)
        tina.pensize(3)
        tina.pencolor(randkleur)
        tina.fillcolor(vulkleur)
        tina.begin_fill()
        tina.forward(30)
        tina.circle(25, 180)
        tina.forward(60)
        tina.circle(25, 180)
        tina.forward(30)
        tina.end_fill()

    def tekenRuit(self, tina, randkleur, vulkleur):
        tina.speed(0)
        tina.pensize(3)
        tina.pencolor(randkleur)
        tina.fillcolor(vulkleur)
        tina.penup()
        tina.left(90)
        tina.forward(15)
        tina.right(90)
        tina.forward(60)
        tina.pendown()
        tina.begin_fill()
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
        tina.forward(15)
        tina.circle(35, 90)
        tina.circle(20, 60)
        tina.circle(10, 60)
        tina.circle(-30, 30)
        tina.forward(30)
        tina.circle(35, 90)
        tina.circle(20, 60)
        tina.circle(10, 60)
        tina.circle(-30, 30)
        tina.forward(30)
        tina.end_fill()

    def renderCard(self):
        """
        Laat tina de correcte tekening maken op de kaart. Maakt gebruik van
        de hulpfuncties tekenOvaal(), tekenRuit(), tekenGolf()
        """
        randkleuren = ['red', 'purple', 'green']
        vulkleuren = [['red',    'pink',          'white'],
                      ['purple', 'MediumPurple', 'white'],
                      ['green',  'LightGreen',   'white']]
        xy = []
        tina = self.myTurtle
        if self.setcard == None:
            self.drawLabel()
        else:
            if self.setcard.hoeveelheid == 3:
                xy = [[0, -105],
                      [0, -30],
                      [0,  45]]
            elif self.setcard.hoeveelheid == 2:
                xy = [[0, -60],
                      [0, 30]]
            elif self.setcard.hoeveelheid == 1:
                xy = [[0, -30]]

            for pos in xy:
                tina.penup()
                tina.goto(pos[0], pos[1])
                tina.pendown()

                if self.setcard.vorm == 1:  # ovaal
                    self.tekenOvaal(tina,
                                    randkleuren[self.setcard.kleur-1],
                                    vulkleuren[self.setcard.kleur-1][self.setcard.vulling-1])
                elif self.setcard.vorm == 2:  # ruit
                    self.tekenRuit(tina,
                                   randkleuren[self.setcard.kleur-1],
                                   vulkleuren[self.setcard.kleur-1][self.setcard.vulling-1])
                elif self.setcard.vorm == 3:  # golf
                    self.tekenGolf(tina,
                                   randkleuren[self.setcard.kleur-1],
                                   vulkleuren[self.setcard.kleur-1][self.setcard.vulling-1])
