# using modules, libraries?, or so-called functions???
from sys import argv
# using variables, describing what argv is
script, filename = argv
# variable
txt = open(filename)
# what we would like to show, or make work visible
print "Here's your file %r:" % filename
print txt.read()
# some more and a variable
print "Type the filename again:"
file_again = raw_input("> ")
# variable
txt_again = open(file_again)
# which text we would like to read??
print txt_again.read()
