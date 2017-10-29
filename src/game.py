from card import SetCard
from deck import Deck
#from field import Field

class Game():
    """
    Game class implements actual game logic.
    """

    def __init__(self, deck, field):
        self.score = 0       # number of sets made
        self.deck  = deck
        self.field = field


    def updateStats(self):
        """
        Updates the relevant statistics. Call after a change has happened to the field.
        """
        #todo: update score
        #todo: count sets
        return None


    def countSets(self, field):
        """
        Counts the number of sets in the current field.
        Brute force checks all possible combinations.
        """
        count = 0
        if field.length() >= 3:
            for c1 in field:
                field2 = field[:]
                field2.remove(c1)
                for c2 in field2:
                    field3 = field2[:]
                    field3.remove(c2)
                    for c3 in field3:
                        if self.isSet(c1,c2,c3):
                            count+=1
        return count/6


    def partialSet(self, a, b, c):
        if a == b and b == c:
            return True
        elif a + b + c == 3:
            return True
        else:
            return False


    def isSet(self, c1, c2, c3):
        """
        Returns True if the Cards c1, c2 & c3 form a set else returns False
        """
        if self.partialSet( c1['number'], c2['number'], c3['number'] ):
            if self.partialSet( c1['symbol'], c2['symbol'], c3['symbol'] ):
                if self.partialSet( c1['shading'], c2['shading'], c3['shading'] ):
                    if self.partialSet( c1['color'], c2['color'], c3['color'] ):
                        return True
        else:
            return False
#        return


    def makeSet(self, c1, c2):
        """
        Returns the required card to form the set.
        """
#        return Card( 0, 0, 0, 0 )
        return SetCard( c1['number']  if c1['number'] ==c2['number']  else (3-c1['number'] )-c2['number'] ,
                        c1['symbol']  if c1['symbol'] ==c2['symbol']  else (3-c1['symbol'] )-c2['symbol'] ,
                        c1['shading'] if c1['shading']==c2['shading'] else (3-c1['shading'])-c2['shading'],
                        c1['color']   if c1['color']  ==c2['color']   else (3-c1['color']  )-c2['color']   )
