class PartyAnimal:
    x = 0
    def __init__(self):
        print "I am constructed"

    def party(self):
        self.x = self.x + 1
        print "So Far " , self.x

    def __del__(self):
        print "I am destructed"

an = PartyAnimal()

an.party()
an.party()
an.party()

#print dir(an)
#print type(an)