"""
game.py
============================================
Basismodule voor de logica van het spel Set.
"""

from setkaart import SetKaart
from deck import Deck


class Game():
    """
    Game class implementeert de logica van het kaartspel.
    """

    def __init__(self, deck=None, field=None):
        self.score = 0
        self.deck = deck
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
                        if self.isSet(c1, c2, c3):
                            count += 1
        return count / 6


    def deelSet(self, a, b, c):
        if a == b and b == c:
            return True
        elif a + b + c == 6:
            return True
        else:
            return False


    def isSet(self, kaart1, kaart2, kaart3):
        """
        Returnt de waarde True als kaart1, kaart2 en kaart3 een set vormen en anders returnt het de waarde False.
        Om mee te beginnen zal het elke 3 kaarten als niet een set aanduiden (met return False).

        :param kaart1: De eerste SetKaart om te vergelijken.
        :type kaart1: SetKaart
        :param kaart2: De tweede SetKaart om te vergelijken.
        :type kaart2: SetKaart
        :param kaart3: De derde SetKaart om te vergelijken.
        :type kaart3: SetKaart
        """
        if self.deelSet( kaart1.hoeveelheid, kaart2.hoeveelheid, kaart3.hoeveelheid ):
            if self.deelSet( kaart1['kleur'], kaart2['kleur'], kaart3['kleur'] ):
                if self.deelSet( kaart1['vorm'], kaart2['vorm'], kaart3['vorm'] ):
                    if self.deelSet( kaart1['vulling'], kaart2['vulling'], kaart3['vulling'] ):
                        return True
        else:
            return False


    def maakSet(self, kaart1, kaart2):
        """
        Returnt de vereiste kaart om een set te maken. De eigenschappen van de kaarten kun je opvragen met:
        ``kaart1.hoeveelheid``, ``kaart1.kleur``, ``kaart1.vorm``, ``kaart1.vulling`` en ``kaart2.hoeveelheid``, ``kaart2.kleur``, ``kaart2.vorm``, ``kaart2.vulling``.

        Als bijvoorbeeld ``maakSet( SetKaart(1,1,1,1), SetKaart(2,2,2,2) )`` aangeroepen wordt dan geldt:
            kaart1.hoeveelheid = 1
            kaart1.kleur = 1
            kaart1.vorm = 1
            kaart1.vulling = 1
            en
            kaart2.hoeveelheid = 2
            kaart2.kleur = 2
            kaart2.vorm = 2
            kaart2.vulling = 2
        """

        # using inline conditionals for legibility
        hv = kaart1['hoeveelheid'] if kaart1['hoeveelheid'] == kaart2['hoeveelheid']  else (6-kaart1['hoeveelheid'] )-kaart2['hoeveelheid']
        kl = kaart1['kleur']       if kaart1['kleur']       == kaart2['kleur']        else (6-kaart1['kleur']       )-kaart2['kleur']
        vo = kaart1['vorm']        if kaart1['vorm']        == kaart2['vorm']         else (6-kaart1['vorm']        )-kaart2['vorm']
        vu = kaart1['vulling']     if kaart1['vulling']     == kaart2['vulling']      else (6-kaart1['vulling']     )-kaart2['vulling']

        return SetKaart(hv, kl, vo, vu)
