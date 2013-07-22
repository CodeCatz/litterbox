my_name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight,my_age + my_height + my_weight)

# %d for numbers and %s for strings?
"""
'd'	Signed integer decimal.	 
'i'	Signed integer decimal.	 
'o'	Signed octal value.	(1)
'u'	Obsolete type – it is identical to 'd'.	(7)
'x'	Signed hexadecimal (lowercase).	(2)
'X'	Signed hexadecimal (uppercase).	(2)
'e'	Floating point exponential format (lowercase).	(3)
'E'	Floating point exponential format (uppercase).	(3)
'f'	Floating point decimal format.	(3)
'F'	Floating point decimal format.	(3)
'g'	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
'G'	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
'c'	Single character (accepts integer or single character string).	 
'r'	String (converts any Python object using repr()).	(5)
's'	String (converts any Python object using str()).	(6)
'%'	No argument is converted, results in a '%' character in the result.
"""