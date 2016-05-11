class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print self.price, self.max_speed, self.miles	
	def ride(self):
		print "Riding"
		self.miles +=10	
	def reverse(self):
		
		if self.miles <5:
			print "Sorry, you can't reverse anymore. You have no more miles"
			return "You've gotta stop riding backward you have no more miles to go!"
		else:
			print "Reversing"
			self.miles -= 5	

oneCoolBike = Bike(300, "40mph")
awesomeBike = Bike(820, "64mph")
anOkBike = Bike(95, "20mph")
oneCoolBike.ride()
oneCoolBike.ride()
oneCoolBike.ride()
oneCoolBike.reverse()			
oneCoolBike.displayInfo()

awesomeBike.ride()
awesomeBike.ride()
awesomeBike.reverse()
awesomeBike.reverse()
awesomeBike.displayInfo()

anOkBike.reverse()
anOkBike.reverse()
anOkBike.reverse()
anOkBike.displayInfo()