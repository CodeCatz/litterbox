i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The final numbers: "

for num in numbers:
	print num

print "======"

# making the same thing with a function
# just adding a bit more spice by allowing you 
# to choose the number of items and the gap between them

def fill_list(items, gap):
	i = 0
	my_list = []

	if gap != 0:
		while len(my_list) < items:
			my_list.append(i)
			i += gap
		return my_list
	else:
		return "Trying to get an infinit loop, eh? You're not getting a list."

print "How many items do you want?"
items = int(raw_input("Type number: "))
print "What should the increment be?"
gap = int(raw_input("Type number: "))


print fill_list(items, gap)

def fill_list_for(items):
	my_list = []

	for i in range(items):
		my_list.append(i)
	return my_list

print "Again: how many items?"
items = int(raw_input("Type number: "))

print fill_list_for(items)

