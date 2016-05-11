class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print self.price, self.max_speed, self.miles	
		return self
	def ride(self):
		print "Riding"
		self.miles +=10	
		return self
	def reverse(self):
		
		if self.miles <5:
			print "Sorry, you can't reverse anymore. You have no more miles"
			return self
		else:
			print "Reversing"
			self.miles -= 5	

		return self

oneCoolBike = Bike(300, "40mph")
awesomeBike = Bike(820, "64mph")
anOkBike = Bike(95, "20mph")
oneCoolBike.ride().ride().ride().reverse().displayInfo()			

awesomeBike.ride().ride().reverse().reverse().displayInfo()

anOkBike.reverse().reverse().reverse().displayInfo()