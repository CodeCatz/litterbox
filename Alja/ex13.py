# importing new features - modules or libraries, woot!
# argv = "argument variable"
from sys import argv
# our argument will have four variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# when running the script, we must provide all four variables
# example: python ex13.py first 2nd 3rd

end = raw_input("How do you find this script? ")
print end, "\nYour initil parameters were:", first, second, third