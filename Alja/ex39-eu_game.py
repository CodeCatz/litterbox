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
	user_country = raw_input("Which country are you interested in? ").title()
	country = eu_countries.get(user_country)
	if not country:
		print "Sorry, that's not a member state."
		print "Do you need a list of member states? [y/n]"
		next = raw_input("> ")
		if next == "y":
			list_countries = eu_countries.keys()
			list_countries.sort()
			print "The current EU member states are (in alphabetical order): \n"
			print ', '.join(list_countries)
			try_again()
		else:
			try_again()
	else:
		print "The capital of %s is: %s" % (user_country, eu_capitals[country])
		try_again()

def try_again():
	print "\nDo you want to try again? [y/n]"
	next = raw_input("> ")
	if next == "y":
		find_capital()
	else:
		print "Too bad. Goodbye."

find_capital()