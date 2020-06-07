#Entity
class Entity:
	stats = {
	"Health" : 0,
	"Attack_Damage" : 0,
	"Ranged_Damage" : 0,
	"Stamina" : 0,
	"Latitude" : 0,
	"Longitude" : 0
	}
	
	def move(lat=0, lon=0):
		self.stats["Latitude"] += lat
		self.stats["Longitude"] += lon
	
	def __init__(self):
		pass
		