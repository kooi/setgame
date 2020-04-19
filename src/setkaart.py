"""SetKaart"""


class SetKaart():
    """
    Class to keep track of card properties.

    Elke kaart heeft 4 eigenschappen, te weten een *hoeveelheid*, een *kleur*, een *vorm* en een *vulling*. Van elke eigenschap zijn er 3 varianten. In plaats van tekst gebruiken we het getal 1, 2 of 3 om deze eigenschap te onthouden. Een hele kaart wordt dan een verzameling van 4 getallen 1, 2 of 3.

    :param hoeveelheid: 1 (een), 2 (twee), 3 (drie)
    :type  hoeveelheid: int
    :param kleur:       1 (rood), 2 (paars), 3 (groen)
    :type  kleur:       int
    :param vorm:        1 (ovaal), 2 (ruit), 3 (golf)
    :type  vorm:        int
    :param vulling:     1 (vol), 2 (halfvol), 3 (leeg)
    :type  vulling:     int
    """

    def __init__(self, hoeveelheid, kleur, vorm, vulling):
        self.hoeveelheid = hoeveelheid
        self.kleur = kleur
        self.vorm = vorm
        self.vulling = vulling

    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append('{key}={value}'.format(
                key=key, value=self.__dict__[key]))
        return ', '.join(sb)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __len__(self):
        return len(self.__dict__)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __repr__(self):
        sb = [
            self.hoeveelheid,
            self.kleur,
            self.vorm,
            self.vulling
        ]
        return str(sb)
