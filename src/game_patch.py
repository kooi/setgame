from setkaart import SetKaart
from game import Game

def isSet(self, kaart1, kaart2, kaart3):
    """
    Returnt de waarde True als kaart1, kaart2 en kaart3 een set vormen en anders returnt het de waarde False.
    Om mee te beginnen zal het elke 3 kaarten als niet een set aanduiden (met return False).
    """
    return True

def maakSet(self, kaart1, kaart2):
    """
    Returnt de vereiste kaart om een set te maken. De eigenschappen van de kaarten kun je opvragen met:
        kaart1.hoeveelheid, kaart1.kleur, kaart1.vorm, kaart1.vulling en
        kaart2.hoeveelheid, kaart2.kleur, kaart2.vorm, kaart2.vulling en
    Als bijvoorbeeld
        maakSet( SetKaart(1,1,1,1), SetKaart(2,2,2,2) ) aangeroepen wordt dan geldt:
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
    hv = 2
    kl = 2
    vo = 2
    vu = 2
    return SetKaart(hv, kl, vo, vu)

# apply patch
Game.isSet = isSet
Game.maakSet = maakSet
