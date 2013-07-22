# a function that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# printing the amount of cheese, arg1
	print "You have %d cheeses!" % cheese_count
	#printing the amount of crackers, arg2
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# just more printing *yawn*
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# calling the function by typing in the two args with numbers
cheese_and_crackers(20, 30)

print "OR we can use variables from our script:"
# definining amount as variables
amount_of_cheese = 10
amount_of_crackers = 50

# and passing in these variables into our function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# now both arguments use some math
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# combining all together, such fun.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "Ok, that isn't much fun. Let's see how many you really have."
# adding my own code, asking for user input
# because I'm working with numbers, I want to convert them into integers
u_cheese = int(raw_input("How many cheeses? "))
u_crackers = int(raw_input("How many crackers? "))

# and I eat a box of crackers, because I can.
cheese_and_crackers(u_cheese, u_crackers - 1)

print "P.S.: Sorry, I ate a box of crackers while working. Helps me think better."