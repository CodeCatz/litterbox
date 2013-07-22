from sys import argv

script, from_file, to_file = argv

# open destination file in write mode
# and write in it what you get when you open and read source file
open(to_file, 'w').write(open(from_file).read())

# exercise 17, making just one line of action code
# basically, I just make a very simple copy script