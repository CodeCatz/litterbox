from sys import argv

# an exercise with opening, writing, reading, erasing and what not files

script, filename = argv

print "We're going to erase %r." % filename

# first we need to open the file, using r+ to be able to read and write
# originally used 'w' for writing only
print "Opening the file..."
target = open(filename, 'r+')

# printing the contents of the file
print "Currently, the file's content is:"
print target.read()

# giving the user the option to abort, abort!
print "If you don't want to erase that, hit CTRL-C (^C) nao!"
print "If you want to proceed, hit RETURN."
# just asking for confirmation, not saving anything here...
raw_input("?")

# zomg, emptying file, hide!
print "Truncating the file. Goodbye!"
target.truncate()

# Ok, close. Take a breath.
target.close()

# We need new content now
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Open file again, let's do it with write only
target = open(filename, 'w')

# write, write each line, new line breaks in between
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# done, close.
target.close()

# let's do one more open, with feeling. Just for reading.
target = open(filename, 'r')

print "\nOk, done. I'll now read the contents of %r." % filename

# print what's in the file
print target.read()

print "And finally, we close it."

# don't forget to close. 
target.close()
# Close the file like you close the fridge door after taking stuff out.

