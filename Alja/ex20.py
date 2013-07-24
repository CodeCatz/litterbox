from sys import argv
# importing stuff for unpacking argv
script, input_file = argv

# function that will read the contents of f, f probably being an open file
def print_all(f):
	print f.read()

# this funciton moves the pointer back to zero, so we can do stuff back from beginning
def rewind(f):
	f.seek(0)

# will print line number and read lines from beginning (because we rewind)
def print_a_line(line_count, f):
	# the comma at the end of print makes sure readline() doesn't add \n at the end
	print line_count, f.readline(),

# that's what we'll be using for f in other functions
current_file = open(input_file)

print "First let's print the whole file:\n"

# calling function print_all on the file we just opened
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# calling function rewind, so we can set pointer back to zero
rewind(current_file)

print "Let's print three lines:"

# starting from line one, print a line from current file
current_line = 1
print_a_line(current_line, current_file)

# same as writing current_line = current_line + 1 
current_line += 1
print_a_line(current_line, current_file)

current_line += 1 
print_a_line(current_line, current_file)

# won't we close the file?
current_file.close()