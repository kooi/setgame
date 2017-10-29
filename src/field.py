


class Field():
    """
    Keeps track of the playing field cards. Implements the set! functions.
    """


    def __init__(self, num):
        self.field = []


    def addCard(self, card):
        #add card to the end if there are no holes. if there are holes fill those first

        #append to the end of the field
        self.field.append(card)


    def removeCard(self, num):
        self.field[num] = None


#####################
    def __getitem__(self,num):
        return self.field[num]


    def length(self):
        """
        Number of cards on the field. This equals the size of the field minus the number of holes.
        """
        return len(self.field) - self.field.count(None)


    def __len__(self):
        """
        Length of field; note that this includes holes. If you wish to omit holes use .length()
        """
        return len(self.field)
