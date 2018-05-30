
class SetKaart():
    """
    Elke kaart heeft 4 eigenschappen, te weten
       een _hoeveelheid_, een _kleur_, een _vorm_ en een _vulling_.
    Van elke eigenschap zijn er 3 varianten.
    In plaats van tekst zouden we dus het getal 1, 2 of 3 kunnen gebruiken om een eigenschap te onthouden.
    Een hele kaart wordt dan slechts 4 getallen 1, 2 of 3.
      hoeveelheid: één   (=1), twee    (=2), drie  (=3)
      kleur:       rood  (=1), paars   (=2), groen (=3)
      vorm:        ovaal (=1), ruit    (=2), golf  (=3)
      vulling:     vol   (=1), halfvol (=2), leeg  (=3)
    """


    def __init__(self, hoeveelheid, kleur, vorm, vulling):
        self.hoeveelheid = hoeveelheid
        self.kleur       = kleur
        self.vorm        = vorm
        self.vulling     = vulling


    def __str__(self):
        sb = []
#        print (self.__dict__)
        for key in self.__dict__:
            sb.append('{key}={value}'.format(key=key,value=self.__dict__[key]))
        return ', '.join(sb)


    def __setitem__(self,key,value):
        self.__dict__[key] = value


    def __getitem__(self,key):
        return self.__dict__[key]


    def __len__(self):
        return len(self.__dict__)


    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False


    def __setattr__(self,key,value):
        self.__dict__[key] = value


    def __repr__(self):
        sb = [
            self.hoeveelheid,
            self.kleur,
            self.vorm,
            self.vulling
        ]
        return str(sb)
