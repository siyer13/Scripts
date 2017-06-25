import pickle
class Animal:
   def __init__(self, number_of_paws, color):
       self.number_of_paws = number_of_paws
       self.color = color
class Sheep(Animal):
   def __init__(self, color):
       Animal.__init__(self, 4, color)

# Step 1: Let's create the sheep Mary
mary = Sheep("white")
# Step 2: Let's pickle Mary
my_pickled_mary = pickle.dumps(mary)
print ("Would you like to see her pickled? Here she is!")
print (my_pickled_mary)
# Step 3: Now, let's unpickle our sheep Mary creating another instance, another sheep... Dolly!
dolly = pickle.loads(my_pickled_mary)
# Dolly and Mary are two different objects, in fact if we specify another color for dolly
# there are no conseguencies for Mary
dolly.color = "black"

print (str.format("Dolly is {0} ", dolly.color))
print (str.format("Mary is {0} ", mary.color))
