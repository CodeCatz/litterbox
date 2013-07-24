# added variables; %d for number, %s for normal word, validat ethem on te end of the string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# used variables to show off
print x
print y
# variable in a variable, %r for debugging?
print "I said: %r." % x
print "I also said: '%s'." % y
# some more variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# using variables to print
print joke_evaluation % hilarious
# more and more variables
w = "This is the left side of..."
e = "a string with a right side."
# and more printing
print w + e
