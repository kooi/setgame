from card import Card
from deck import Deck
#from field import Field

class Game():
    """
    Game class implements actual game logic.
    """

    def __init__(self):
        self.score = 0       # number of sets made
        self.deck  = Deck()  # Deck object
#        self.field = Field() # Field object

    def countSets(self, field):
        """
        Counts the number of sets in the current field.
        Brute force checks all possible combinations.
        """

#todo
#        for i in range(  ):
#            for j in range(  ):


    def isSet(self, c1, c2, c3):
        """
        Returns True if the Cards c1, c2 & c3 form a set else returns False
        """
        return True
#todo


    def makeSet(self, c1, c2):
        """
        Returns the required card to form the set.
        """

#        c3 = Card()

        return Card( c1['number']  if c1['number'] ==c2['number']  else (3-c1['number'] )-c2['number'] ,
                     c1['symbol']  if c1['symbol'] ==c2['symbol']  else (3-c1['symbol'] )-c2['symbol'] ,
                     c1['shading'] if c1['shading']==c2['shading'] else (3-c1['shading'])-c2['shading'],
                     c1['color']   if c1['color']  ==c2['color']   else (3-c1['color']  )-c2['color']   )
#        return Card(  )

#todo
# for each property check if values are the same
#   if so: the 3rd card also has this property
#   if not: the 3rd card requires the property that adds the total to 3 [0,1,2]
