ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there's not 10 things in that list, let's fix that."

# split the string into a list whenever you see a space between words 
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# keep filling the list until we have 10 items
while len(stuff) != 10:
	# pop the list item off the more_stuff list, save it as the next_one variable
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	# append(next_one, stuff) - Append the next_one variable ot the the stuff list
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

# print the second item in the list
print stuff[1]
# print the last item in the list
print stuff[-1] # whoa! fancy
# pop the last item off the stuff list pop(last_item, stuff)
print stuff.pop()
# join all items in stuff with a space join(' ', stuff)
print ' '.join(stuff) # what? cool!
# join all items in stuff from the 4th element up to the 6th (items with index 3 and 4) with a # join('#', stuff[3:5])
print '#'.join(stuff[3:5]) # super stellar