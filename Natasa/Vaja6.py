# This one puts 10 into a string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s ." % (binary, do_not)
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y
# we defined hilarious as False, than created variable joke_evaluation
#'r' String (converts any Python object using repr()).
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#string addition - two strings merge into one string.
print w + e