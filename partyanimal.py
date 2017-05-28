class PartyAnimal:
	x = 0
	name = ""

	def __init__(self,nam):
		self.name = nam
		print nam," just got constructed"
		#print "I am constructed"

	def __del__(self):
		print "I am destructed",self.x

	def party(self):
		self.x = self.x + 1 
		print self.name, "party count", self.x

class FootballFan(PartyAnimal):
	points = 0

	def touchdown(self):
		self.points = self.points + 7
		self.party()
		print self.name, " points ", self.points

#an = PartyAnimal()
# Equivalent to PartyAnimal.party(an)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()

#j = PartyAnimal("Jim")
#j.party()
#s.party()
#s.party()
#an.party()
#an.party()
#an.party()

#print dir(an)