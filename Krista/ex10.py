tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/", "-", "|", "\\", "|"]:Janª
		print "%s\r" % i,

# character \n (back slash) - put a new line character into the string at that point
# \\ will print just one backslash
# escape double-quotes and single-quotes 
# "I am 6'2\" tall." # escape double-quote inside string
# 'I am 6\'2" tall.' # escape single-quotes inside string
# or using triple single-quotes