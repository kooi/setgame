from setkaart import SetKaart
from deck import Deck

class Game():
    """
    Game class implements actual game logic.
    """

    def __init__(self, deck=None, field=None):
        self.score = 0       # number of sets made
        self.deck  = deck
        self.field = field


    def telSets(self, field):
        """
        Telt het aantal sets op het veld door simpelweg alle combinaties
        te proberen en vervolgens te delen door het aantal keer dat een
        set is meegenomen.
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


    def deelSet(self, a, b, c):
        """
        Hulpfunctie
        """
        if a == b and b == c:
            return True
        elif a + b + c == 6:
            return True
        else:
            return False


    def isSet(self, kaart1, kaart2, kaart3):
        """
        Returnt de waarde True als kaart1, kaart2 en kaart3 een set vormen en anders returnt het de waarde False.
        """
        if self.deelSet( kaart1['hoeveelheid'], kaart2['hoeveelheid'], kaart3['hoeveelheid'] ):
            if self.deelSet( kaart1['kleur'], kaart2['kleur'], kaart3['kleur'] ):
                if self.deelSet( kaart1['vorm'], kaart2['vorm'], kaart3['vorm'] ):
                    if self.deelSet( kaart1['vulling'], kaart2['vulling'], kaart3['vulling'] ):
                        return True
        else:
            return False
###        return False


    def maakSet(self, kaart1, kaart2):
        """
        Returnt de vereiste kaart om een set te maken.
        """
        return SetKaart( kaart1['hoeveelheid'] if kaart1['hoeveelheid'] == kaart2['hoeveelheid']  else (6-kaart1['hoeveelheid'] )-kaart2['hoeveelheid'],
                         kaart1['kleur']       if kaart1['kleur']       == kaart2['kleur']        else (6-kaart1['kleur']       )-kaart2['kleur'],
                         kaart1['vorm']        if kaart1['vorm']        == kaart2['vorm']         else (6-kaart1['vorm']        )-kaart2['vorm'],
                         kaart1['vulling']     if kaart1['vulling']     == kaart2['vulling']      else (6-kaart1['vulling']     )-kaart2['vulling'] )
###        return SetKaart(1, 1, 1, 1)
