#From package sys take feature argv
from sys import argv

#runs the script with filename argv
script, filename = argv
#creates variable
txt = open(filename)

print "Here's your file %r" %filename
#reads the file
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()