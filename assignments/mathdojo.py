# part 1
class MathDojo(object):
	def __init__(self):

		self.total = 0 

	def add(self, *nums):
		for number in nums:
			self.total +=  number

		return self

	def subtract(self, *nums):
		for number in nums:
			self.total -=  number
		return self

	def displayInfo(self):
		print self.total
		return self

addingUp = MathDojo()

addingUp.add(2).add(2,5).subtract(3,2).displayInfo()





class MathDojo(object):
	def __init__(self):

		self.total = 0 

	def add(self, *nums):
		#first loop loops through all the numbers as variables
		for number in nums: 
			#if it finds a list or a tuple
			if isinstance(number,list) or isinstance(number, tuple):
				for newnum in number:
					self.total += newnum
			#if it only finds a single digit
			else:
				self.total += number 
		return self

	def subtract(self, *nums):
		for number in nums: 
			if isinstance(number,list) or isinstance(number, tuple):
				for newnum in number:
					self.total -= newnum	
			else:
				self.total -= number 
		return self

	def displayInfo(self):
		print self.total
		return self

withList = MathDojo()
withList.add(2,[1,2,3]).displayInfo()
withList.add(2).displayInfo()
withList.subtract([5,2,8], 5).displayInfo()

