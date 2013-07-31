# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
# states.items() provides a list of (key, value) pairs
# states.keys() provides a list of keys in the dict
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

# safely get an abbreviation by state that might not be there
print '-' * 10
# dict.get(key, default)
# return the value for key if key in dict, else return default
# if no second arg given, default is None, 
# so writing None below isn't really needed
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

# get a city with a default value
# similar to above, only in this case we replace None with 'Does Not Exist'
# if TX was is the cities dict, city would return the value of TX
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

print '-' * 10
print "All (key, value) pairs in dict states: \n", states.items()

print '-' * 10
print "All keys - entries in dict states: \n", states.keys()

print '-' * 10
print "All value in dict states: \n", states.values()

print '-' * 10
print "The number of entries in dict states: ", len(states)

