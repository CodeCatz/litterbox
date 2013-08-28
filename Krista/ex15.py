# from the module named sys import the thing named argv into the current name context. 
from sys import argv

# unpack into the two named variables, script = ex15.py file, filename = ex15_sample.txt 
script, filename = argv

# opens text file
txt = open(filename)

# Prints "here is your file" adds filename
print "Here's your file %r" % filename
# prints what is in the file
print txt.read()

print "Type the filename again:"
# reads line from users input 
file_again = raw_input("> ")
# opens file again
txt_again = open(file_again)
# print text from a file again
print txt_again.read()