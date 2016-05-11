class Car(object):
	def __init__(self, price, speed, fuel, mileage):
	
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

		if self.price > 10000: 
			self.tax = .15
		else: 
			self.tax = .12

	def displayAll(self):
		return "Your cars base cost is " + str(self.price) + " travels " + self.speed + " gets " + self.mileage + " and has a " + self.fuel + " fuel tank. Your total cost was " + str(self.price * self.tax)

myAudi = Car(54000, "45mph", "Full", "23mpg")
mySubaru = Car(23000, "50mph", "Mostly Full", "30mpg")
myVolvo = Car(2000, "20mph", "Almost Empty", "20mpg")
print myAudi.displayAll()
print mySubaru.displayAll()
print myVolvo.displayAll()