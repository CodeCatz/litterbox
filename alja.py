ime = "Alja"

print ime

print (ime + " ") * 5

new_line = "\n"

# text for new exercise divider
new_exercise = """
===
:: EXERCISE %d ::
"""

print new_exercise % 3

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

print new_exercise % 4

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


print new_exercise % 5

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

print new_exercise % 6

# making string and including various variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# printing variables from the previous block with includes
print x
print y

# and again printing variables, including them as variables...
print "I said: %r." % x
print "I also said: '%s'." % y

# two variables, one without a defined variable inclusion
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# using the second variable in the first
print joke_evaluation % hilarious

# just combining two strings
w = "This is the left side of..."
e = "a string with a right side."

print w + e

print new_exercise % 7

# printing strings
print "Marry had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what's that do? 
# the line above will write a dot ten times!
# defining a bunch of variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# printing all short variables together, 
# the comma at the end makes sure it's all one line
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

print new_exercise % 8

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)

print new_exercise % 9

# Here's some new strange stuff, remember type it exactly.
# defining days and months
days = "Mon Tue Wed Thu Fri Sat Sun"
# after each month comes a new line
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#printing variables with an intor string
print "Here are the days: ", days
print "Here are the months: ", months
# print text as formatted, including line breaks and all
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print new_exercise % 10

# \t makes a tab
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
# ignoring the backslash
backslash_cat = "I'm \\ a \\ cat."
# each item has a tab, the last includes a new line
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat



