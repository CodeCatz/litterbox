# \t moves to left? \n split string into new line \\ smt \\ still leaves one \
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
# no """ \t moves left
fat_cat = """I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
