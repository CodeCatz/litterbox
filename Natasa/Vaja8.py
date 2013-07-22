# we defined formatter to be a string of 4 
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"that you could type up right.",
"but it didn't sing.",
"So I said goodnight."
)

# %r is for debugging purposes - it will sometimes write "" or ' ' 