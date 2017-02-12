class PartyAnimal:
    x = 0
    name =""

    def __init__(self,z):
        self.name = z
        print self.name, "I am constructed"

    def party(self):
        self.x = self.x + 1
        print self.name, "So Far " , self.x

s = PartyAnimal("Sally")

s.party()

j = PartyAnimal("Jim")
j.party()
s.party()

#print dir(an)
#print type(an)
