import unittest
from ...setgame.game import Game
from ...setgame.setkaart import SetKaart

# importeer hier de gewijzigde versies van game.isSet() en game.maakSet()
# uit game_patch.py
# comment deze weg om de originele versie te gebruiken
import game_patch

class TestGame(unittest.TestCase):
    """
    Unit test data om de werking van isSet() en maakSet() te testen.
    Uitvoeren met: python3 testset_klein.py
    """
################################################################################
############### Vul hieronder je testsets op de corrcete plek in ###############
################################################################################


    correcte_sets = [
        ( SetKaart(2, 3, 3, 3), SetKaart(1, 1, 2, 2), SetKaart(3, 2, 1, 1) ),
        ( SetKaart(2, 3, 3, 3), SetKaart(3, 1, 1, 3), SetKaart(1, 2, 2, 3) ),
        ( SetKaart(3, 3, 2, 2), SetKaart(1, 1, 2, 2), SetKaart(2, 2, 2, 2) ),
        ( SetKaart(1, 1, 3, 2), SetKaart(2, 2, 2, 2), SetKaart(3, 3, 1, 2) ),
        ( SetKaart(3, 1, 1, 3), SetKaart(3, 2, 1, 1), SetKaart(3, 3, 1, 2) ),
        ( SetKaart(2, 2, 2, 2), SetKaart(1, 2, 2, 3), SetKaart(3, 2, 2, 1) )
    ]

    incorrecte_sets = [
        ( SetKaart(2, 3, 3, 3), SetKaart(3, 3, 2, 2), SetKaart(1, 1, 2, 2) ),
        ( SetKaart(1, 1, 3, 2), SetKaart(1, 2, 2, 2), SetKaart(3, 1, 2, 1) ),
        ( SetKaart(3, 1, 1, 3), SetKaart(3, 2, 1, 1), SetKaart(2, 2, 2, 2) ),
        ( SetKaart(1, 1, 3, 2), SetKaart(1, 1, 3, 2), SetKaart(3, 3, 1, 2) ),
        ( SetKaart(3, 1, 1, 3), SetKaart(3, 1, 1, 3), SetKaart(3, 3, 1, 2) ),
        ( SetKaart(2, 2, 2, 2), SetKaart(2, 2, 2, 2), SetKaart(3, 2, 2, 1) )
    ]

    onvolledige_sets = [
        ( SetKaart(2, 3, 3, 3), SetKaart(3, 3, 2, 2), SetKaart(1, 3, 1, 1) ),
        ( SetKaart(1, 1, 2, 2), SetKaart(1, 1, 3, 2), SetKaart(1, 1, 1, 2) ),
        ( SetKaart(1, 2, 2, 2), SetKaart(3, 1, 2, 1), SetKaart(2, 3, 2, 3) ),
        ( SetKaart(3, 1, 1, 3), SetKaart(3, 2, 1, 1), SetKaart(3, 3, 1, 2) )
    ]


################################################################################
######################### Hierna niets meer veranderen #########################
################################################################################


    def setUp(self):
        self.testgame = Game()


    def test(self):
        self.assertTrue(True)


    def test_isSet_correct(self):
        for k1, k2, k3 in self.correcte_sets:
            with self.subTest( i=self.correcte_sets.index( (k1,k2,k3) ) ):
                resultaat = self.testgame.isSet(k1,k2,k3)
                self.assertTrue(resultaat,
                    msg='\n\nDe functie isSet() herkent deze kaarten onterecht niet als een set.'+
                        '\n Kaart 1: '+repr(k1)+
                        '\n Kaart 2: '+repr(k2)+
                        '\n Kaart 3: '+repr(k3)+
                        ''
                    )


    def test_isSet_incorrect(self):
        for k1, k2, k3 in self.incorrecte_sets:
            with self.subTest( i=self.incorrecte_sets.index( (k1,k2,k3) ) ):
                resultaat = self.testgame.isSet(k1,k2,k3)
                self.assertFalse(resultaat,
                    msg='\n\nDe functie isSet() herkent deze kaarten onterecht wel als een set.'+
                        '\n Kaart 1: '+repr(k1)+
                        '\n Kaart 2: '+repr(k2)+
                        '\n Kaart 3: '+repr(k3)+
                        ''
                    )


    def test_maakSet(self):
        for k1, k2, gk in self.onvolledige_sets:
            with self.subTest( i=self.onvolledige_sets.index( (k1,k2,gk) ) ):
                resultaat = self.testgame.maakSet(k1,k2)
                self.assertEqual(resultaat, gk,
                    msg='\n\nDe functie maakSet() vult de volgende twee kaarten foutief aan.'+
                        '\n Kaart 1: '+repr(k1)+
                        '\n Kaart 2: '+repr(k2)+
                        '\n maakSet() geeft: '+repr(resultaat)+
                        '\n correcte kaart:  '+repr(gk)+
                        ''
                    )


if __name__ == '__main__':
    unittest.main()
