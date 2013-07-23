# Input method to pass variables to a script (py files)

# Import - this is how you add features to your script from
# Python feature set.
# argv = "argument variable" - it holds arguments you pass when you run it

from sys import argv

# "unpacks" argv : Take whatever in ARGV, unpack it and assign it
# to all of those variables on the left in order
script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable: ", third

# You run this from command line - python Vaja_13.py hamburger marmelada sir
