eu_countries = {
	'Belgium': 'BE',
	'Bulgaria': 'BG',
	'Czech Republic': 'CZ',
	'Denmark': 'DK',
	'Germany': 'DE',
	'Estonia': 'EE',
	'Ireland': 'IE',
	'Greece': 'EL',
	'Spain': 'ES',
	'France': 'FR',
	'Croatia': 'HR',
	'Italy': 'IT',
	'Cyprus': 'CY',
	'Latvia': 'LV',
	'Lithuania': 'LT',
	'Luxembourg': 'LU',
	'Hungary': 'HU',
	'Malta': 'MT',
	'Netherlands': 'NL',
	'Austria': 'AT',
	'Poland': 'PL',
	'Portugal': 'PT',
	'Romania': 'RO',
	'Slovenia': 'SI',
	'Slovakia': 'SK',
	'Finland': 'FI',
	'Sweden': 'SE',
	'United Kingdom': 'UK'
}

eu_capitals = {
	'AT': 'Vienna',
	'BE': 'Brussels',
	'BG': 'Sofia',
	'HR': 'Zagreb',
	'CY': 'Nicosia',
	'CZ': 'Prague',
	'DK': 'Copenhagen',
	'EE': 'Tallinn',
	'FI': 'Helsinki',
	'FR': 'Paris',
	'DE': 'Berlin',
	'EL': 'Athens',
	'HU': 'Budapest',
	'IE': 'Dublin',
	'IT': 'Rome',
	'LV': 'Riga',
	'LT': 'Vilnius',
	'LU': 'Luxembourg',
	'MT': 'Valletta',
	'NL': 'Amsterdam',
	'PL': 'Warsaw',
	'PT': 'Lisbon',
	'RO': 'Bucharest',
	'SK': 'Bratislava',
	'SI': 'Ljubljana',
	'ES': 'Madrid',
	'SE': 'Stockholm',
	'UK': 'London'
}

def find_capital():
	print "I'll now tell you the capital of any EU member state."
	# letting the user type in a country, using .title() to capitalize first letter
	user_country = raw_input("Which country are you interested in? ").title()
	# checking if the user's country is in the dict eu_countries
	country = eu_countries.get(user_country)
	# if it isn't, the value is None
	if not country:
		print "Sorry, that's not a member state."
		# so I offer to list all member states
		print "Do you need a list of member states? [y/n]"
		next = raw_input("> ")

		# if the user wants the list ...
		if next == "y":
			# I get the list of all eu_countries dict keys
			list_countries = eu_countries.keys()
			# and sort the list in alphabetical order
			list_countries.sort()
			print "The current EU member states are (in alphabetical order): \n"
			# printing them separated by commas, not as a raw list
			print ', '.join(list_countries)
			# calling the function that offers another lookup
			try_again()
		else:
			try_again()

	else:
		# if the country is a member state, I lookup the capital using the country code
		print "The capital of %s is: %s" % (user_country, eu_capitals[country])
		try_again()

# just a simple function that check if the user wants another lookup
def try_again():
	print "\nDo you want to try again? [y/n]"
	next = raw_input("> ")
	# if yes, then calling the find_capital() function again
	if next == "y":
		find_capital()
	# if not, it's game over
	else:
		print "Too bad. Goodbye."

find_capital()