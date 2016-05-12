#lambda examples
#Lambda - is also an anonymous function

multiply = lambda num: num * 2

adding = lambda a,b: a*a + b*b
#could also be wrriten as 
	#def anotherAdd(a,b)
	# a*a + b*b

print multiply(3)
print multiply(8)
print adding(5,2)

#callback - a callback is a function that's passed into another function as a parameter
animals = ['monkey', 'eage', 'giraffe', 'emu', 'seal']
sorted(animals, key=lambda x: x.find("e")) #returns ['eagle', 'emu', 'seal', 'monkey', 'giraffe'] - orders this based on where the e is
	#sorted takes an optional parameter key and sorts the results of that function
#could also be written as
def find_first_e(word):
	return word.find("e")

sorted(animals, key=find_first_e)

#find the lowest and highest associated value 

#an element in a list
my_list = ['test_string', 99, lambda x: x **2]

print my_list[2](4)

#as a callback

def  invoker(callback):
	print callback(3)

invoker1 = invoker(lambda x: 2 * x)



my_arr = [1,2,3,4,5]
def square(num):
	return num **2
# print map(square, my_arr)

print map(lambda x:x**2, my_arr)
print reduce(lambda x,y: x+y, my_arr)



