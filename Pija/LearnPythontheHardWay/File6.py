from sys import argv

script, first, second, third, fourth = argv

print "This script is called:", script
print "Name a fruit:", first
#print "Your name:", second
print "Your favorite ice-cream flavor:", third
print "Your pet's name:", fourth

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")

print "You are %r years old and your height is %r." % (age, height), second