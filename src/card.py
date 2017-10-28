


class Card():
    """
    Every Card object has:
      number  = {0,1,2}
      symbol  = {0,1,2}
      shading = {0,1,2}
      color   = {0,1,2}
    """


    def __init__(self, number, symbol, shading, color):
        #todo: assert that card is valid?; every attribute is an int 0, 1, 2
        #otherwise throw AttributeError?
        self.number  = number
        self.symbol  = symbol
        self.shading = shading
        self.color   = color


    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append('{key}={value}'.format(key=key,value=self.__dict__[key]))
        return ', '.join(sb)


    def __setitem__(self,key,value):
        self.__dict__[key] = value


    def __getitem__(self,key):
        return self.__dict__[key]


    def __len__(self):
        return len(self.__dict__)


####################################

    #required? covered by __setitem__?
    def __setattr__(self,key,value):
        self.__dict__[key] = value

    # called by print(,)
    def __repr__(self):
        # todo
        return '__repr__'
