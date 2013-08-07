formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) 
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)

#Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?
#najbrz zato ker je tm ze didn't in je pol dvojni narekovaj. 