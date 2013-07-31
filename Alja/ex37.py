# KEYWORDS

# and : logic operator, statement is True if all parts are True
# del : deletes target
# from : part of the import statement; from which module or file import what
# not : logical operator, returns True is argument is False, and False if argument is True
# while : while a condition is True, do stuff
### as : part of the with statement
# elif : else if - another option in an if statement if the initial if case isn't met
# global : defines variable as a global variable, can be used outside a function
# or : logic operator, statement is True if at least one part is True
### with : a more eelegant want of doing try and finally, I suppose
### assert : assert statements are used for debugging ###
# else : the final part of an if statement that cathes all other cases that aren't defined by if or elseif
# if : a condition; if it's true, do stuff
# pass : it does nothing, but can be used in functions as a placeholder for future good stuff
#### yield : used in generators, yields a value, you can iterate, and when you call it next, returns next value; a bit tricky
# break : break the for and while loop if a certain condition is met
### except : part of trt statemetns
# import : importing modules or files, so functions can be used inside script
# print : writing stuff or results of functions in console
### class : used in class definitions
# exec : executes the expression
# in : if something is in something else...
# raise : used for raising errors; example: if something: raise error('My error!')
### continue : continues executing code, can be used for readability by reducing indentation
### finally : part of try statements
# is : comparison, ex: if sth is None:
# return : the result of a function
# def : a keyword that starts a user defined function
# for : iterating over a string or list; for each character or item, do stuff
# lambda : anonymous function
### try : try statement, tries stuff, used in combination with except and finally 

# just a list that I'll use
sample_list = ["happy", "sad", "orange", "apples", "juice"]

# from the module random import the function choice
from random import choice
# printing a random choice of a simple list
print "Random choise from a list: ", choice(sample_list)

# defining a simple function that takes one argument
def just_a_function(text):
	# simple if statement: check if letter a is in the string, print sth
	if "a" in text:
		print "Your text includes the letter a."
	# else if - if a isn't in text, but either b - or - c are, print sth else
	elif "b" in text or "c" in text:
		print "Your text includes either b or c, but not an a."
	else:
		print "Your text doesn't include the letters a, b or c. Bummer. I like those."
	
	# another if check: if both letters d and e are in text, print sth
	if "d" in text and "e" in text:
		print "Your text includes both d and e."

	if not("z" in text):
		print "Good, first z check passed."
	
	print "I'll now print the letters in your text:"
	for letter in text:
		if letter == "z":
			print "I don't like the letter z. Printing broken."
			# breaking the for loop if one of the letters is z
			break
		elif letter == "o":
			print "I like o. I should do something special when you write it."
			pass
		print letter

	# at the end return the reverse string, just for fun
	return "Reversed input: " + text[::-1]

user_text = raw_input("Enter some text: ")
print just_a_function(user_text)

# a function with a for loop that print items in a list and the length of each item
def go_through_list(my_list):
	for item in my_list:
		print "The item %s is %d char long." % (item, len(item))

go_through_list(sample_list)

# an example funtion that uses try and except
def example_try():
	while True:
		try:
			x = int(raw_input("Please enter a number: "))
			break
		except ValueError:
			print "Oops!  That was no valid number.  Try again..."

example_try()

print "Example use of exec"
exec 'if True: print 6'

add_one = lambda x: x + 1
print add_one(3)

# DATA TYPES

# True : boolean True
# False : boolen False
# None : absence of value
# strings : text "like this" "or this" 
# numbers : 1, 2, 3
# floats : numbers with decimals; 1., 1.1, 3.0, 2.43434
# lists : a collection of elements; [], [1, 2, 3], ["stuff", 3, "more stuff", 244.98]



# STRING ESCAPE SEQUENCES

# \\ : \ write backslash, don't escape it
# \' : single quote '
# \" : double quote "
# \a : ASCII Bell (BEL)
# \b : ASCII Backspace (BS)
# \f : ASCII Formfeed (FF)
# \n : newline
# \r : return
# \t : horizontal tam
# \v : vertical tab

print """
Let's do some escaping! \\ or \' or \" for characters
\n\\n for new line
\tbackslash b for a tab
\vbackslash v for a vertical tab
\fBackslash f
"""

# STRING FORMATS

# %d 
# %i
# %o 
# %u 
# %x 
# %X 
# %e
# %E
# %f
# %F
# %g
# %G
# %c
# %r
# %s
# %%

# this explains it: http://docs.python.org/release/2.5.2/lib/typesseq-strings.html

print "A number %d, an integer %i, a float %f, a string %s, and anything %r" % (5, 4, 5.4, "string", "anything")

# OPERATORS

# + : plus; 1 + 1 = 2
# - : minus; 1 - 1 = 0
# * : multiply; 10 * 20 = 200
# ** : exponent; 2 ** 3 = 8
# / : divide; 20 / 5 = 4
# // : floor divison; 8 // 2 = 4
# % : modulus - divides left and right, returns remainder; 8 % 3 = 2; 9 % 3 = 0 
# < : less than; 2 < 3 : True
# > : greater than; 3 > 2 : True
# <= : less than or equal; 2 <= 3 and 3 <= 3 : True
# >= : greater than or equal; 3 >= 2 and 2 >= 2 : Treu
# == : check if it's equal; 3 == 3 : True
# != : not equal; 2 != 3 : True
# <> : similar to != 2 <> 3 : True
# ( ) : argument
# [ ] : list
# { } : dictionary
# @ : used for class, function and method decorators
# ,
# :
# .
# =
# ;
# += : value += 1 is the same as value = value + 1
# -= : value -= 1 is like value = value - 1
# *= : see above, with *
# /= : see above
# //= : see above
# %= : value %= 4 is the same as value = value % 4
# **= : see above

