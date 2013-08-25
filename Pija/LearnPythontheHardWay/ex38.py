ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one) # append(stuff, next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

# print the second item in the list
print stuff[1]
# print the last item in the list
print stuff[-1] # whoa! fancy
print stuff.pop() # pop(last_item, stuff)
print ' '.join(stuff) # what? cool! join(' ', stuff)
print '#'.join(stuff[3:5]) # super stellar! join('#', stuff[3:5])