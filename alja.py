ime = "Alja"

print ime

print (ime + " ") * 5

print "==="
print ":: EXERCISE 3 ::"
# printing more stuffz with basic math operations
print "I will now count my chickens:"
# ptinring stuff and adding numbers
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"
# evaluating a statement as True or False
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "==="
print ":: EXERCISE 4 :: "
#now let's play with variables a little bit more

#how many cars do we have?
cars = 100
#how many people can each car take?
space_in_a_car = 4.0
#how many drivers are available?
drivers = 30
#how many passengers need a ride?
passengers = 90
#we can only use cars with a driver
cars_not_driven = cars - drivers
#that's why the number of cars that will be on the road equals the number of available drivers
cars_driven = drivers
#we know how many cars we have, multiply that by number of people that fit in a car
carpool_capacity = cars_driven * space_in_a_car
#how do we distribute passangers amond available cars
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passengers_per_car, "in each car."


print "==="
print ":: EXERCISE 5 ::"
#Moar variables and prints. Hope I don't run out of ink.

name = 'Zed A. Shaw'
age = 35 # not a little
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = round(height * 2.54)
weight_kg = round(weight / 2.2046)

print "Let's talk about %s." % name
print "He's %r inches or %r cm tall." % (height, height_cm)
print "He's %r pounds or %r kg heavy." % (weight, weight_kg)
print "Actually that's not not heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)