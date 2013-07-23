print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you are %r old, %r tall and %r heavy" %(
	age, height, weight)

# We put comma at the end of each print line - so that print doesn't end 
# the line with a newline character and go to the next line.
# Raw_input takes users input and saves it into a variable you set.

print "How are you doing today?",
mood = raw_input()

mood = raw_input("How are you feeling today? ")

print "I feel %s" % mood

#Difference between input and raw_input
#What's the difference between input() and raw_input()?
#The input() function will try to convert things you enter as if
#they were Python code, but it has security problems so you should
#avoid it.

#try to keep lines 80 characters long