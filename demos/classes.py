#create a new class with a parameter of Object (a special python variable used to initialize)
#class ClassName(Object):
class Human(object):
    def __init__(self, clan=None):
      print "New Human!!!"     # when we create a new human, we'll get self as an output
                               # initialize the clan instance variable by passing in a value
      self.clan = clan
      # initialize more attributes that will be the same for all humans
      self.health = 100
      self.strength = 3
      self.intelligence = 3
      self.stealth = 3
    def taunt(self):
      print "You want a piece of me?"
# create an instance of a human, pass in a class name
michael = Human('CodingDojo')
jimmy = Human('CodingNinjas')

class Test(object):
  def __init__(self, phrase='Nothing was passed'):     # set the default value for 'phrase' parameter
    print "This string was passed in: " + phrase
    self.phrase = phrase
    
test1 = Test('Hello, World!')
test2 = Test()
print "Test 1 has phrase: '" + test1.phrase + "'"
print "Test 2 has phrase, '" + test2.phrase + "'"