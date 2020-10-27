class Player:
	def __init__(self):
		self.hp = 10
		self.maxhp = 10
		self.dmg = 3
		self.ac = 0
	upg = 0
	gold = 0
	armor = "winter gear"
	hpupg = 0
	lockpicks = False

class Deer:
	def __init__(self):
		self.hp = 12
		self.dmg = 2

class Crow:
	def __init__(self):
		self.hp = 6
		self.dmg = 3

class Wolf:
	def __init__(self):
		self.hp = 18
		self.dmg = 6