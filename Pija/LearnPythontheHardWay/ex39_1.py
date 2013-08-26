countries = {
	'Sweden': 'SE',
	'Denmark': 'DK',
	'Norway': 'NO',
	'Finland': 'FI',
	'The Netherlands': 'NL'
}

capitals = {
	'SE': 'Stockholm', 
	'DK': 'Copenhagen',
	'NO': 'Oslo'
}

capitals['FI'] = 'Helsinki'
capitals['NL'] = 'Amsterdam'

print '-' * 20
print "FI has: ", capitals['FI']
print "NL has: ", capitals['NL']

print '-' * 20
print "Sweden's abbreviation is: ", countries['Sweden']
print "Denmark's abbreviation is: ", countries['Denmark']

print '-' * 20
print "Sweden has: ", capitals[countries['Sweden']]
print "Denmark has: ", capitals[countries['Denmark']]

print '-' * 20
for country, abbrev in countries.items():
	print "%s is abbreviated %s" % (country, abbrev)

print '-' * 20
for abbrev, capital in capitals.items():
	print "%s's capital is: %s" % (abbrev, capital)

print '-' * 20
for country, abbrev in countries.items():
	print "%s is abbreviated %s. Its capital is %s." % (country, abbrev, capitals[abbrev])

print '-' * 20
country = countries.get('Slovenia', None)

if not country:
	print "Sorry, no Slovenia."

capital = capitals.get('SI', 'Ljubljana')
print "The capital for the country 'SI' is: %s" % capital