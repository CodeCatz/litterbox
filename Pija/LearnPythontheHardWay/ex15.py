from sys import argv

#running the script with a filename argument
script, filename = argv 
#open the specified file and save it in the variable txt
txt = open(filename) 

#printing the contents of the file
print "Here's your file %r:" % filename
# reading the contents with the .read() method that works on files and printing
print txt.read()

#closing the file after we don't need it anymore
txt.close()

# asking for the file name with a user prompt
print "Type the filename again:"
file_again = raw_input("> ")

# new variable for the new file specified by user
txt_again = open(file_again)

# print contents of the file typed in by the user
print txt_again.read()

txt_again.close()