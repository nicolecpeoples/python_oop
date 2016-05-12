class Underscore(object):

	def map(self, arr, func):
		result = [] #the result is a new array 
		for x in arr:
			result.append(func(x))
		return result

	def reduce(self, arr, func, y):
		for x in arr: #loop through array
			y = func(x, y) 
		return y

	def find(self, arr, func):
		for i in arr: #iterate through the array
			if func(i): #if item is in the array
				return i #return item

	def filter(self, arr, func):
		result = []  #append to new array
		for i in arr: #for list item in arr
			if func(i): #if the function has a result of true
				result.append(i) #append item to results array
		return result

	def reject(self, arr, func):
		result=[] #append to a new array
		for i in arr: #for list item in arr
			if not func(i): #if the item returns false
				result.append(i) #append item to array
		return result #return new array

_ = Underscore()

# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 1)
# print evens

# finds = _.find([1, 2, 3, 4, 5, 6], lambda x: x == 4)
# print finds

# mappings = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 3)
# print mappings

# reducing = _.reduce([1, 2, 3, 4, 5, 6], (lambda x, y: x + y), 2)
# print reducing

rejecting = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print rejecting






