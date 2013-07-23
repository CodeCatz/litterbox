people = 30
cars = 40
buses = 15
# I liked cats and dogs more.

# if we have more cars then people, let's go with cars
if cars > people:
	print "We should take the cars."
# but if we have less cars then people, we "can't" take the cars
elif cars < people:
	print "We should not take the cars."
# if the number is the same, it's tough to make a decision :)
else:
	print "We can't decide."

# basically it's just comparing stuff...
# one condition...
if buses > cars:
	print "There's too many buses."
# and another condition...
elif buses < cars:
	print "Maybe we could take the buses."
# and if all that fails, go to else
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."