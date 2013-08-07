from sys import argv

script, filename = argv

target = open(filename, 'r')

print "Let's read the contents of %r." % filename

print target.read()

target.close()