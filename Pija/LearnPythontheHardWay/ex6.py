x = "There are %d types of people." % 10 #vstavi 10 noter namesto %d
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #vstavi noter binary in don't

print x #napise There are 10 types of people.
print y #napise Those who know binary and those who don't.

print "I said: %r." % x #napise I said: 'There are 10 types of people.'.
print "I also said: '%s'." % y #napise I also said: 'Those who know binary and those who don't.'.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious #napise Isn't that joke so funny?! False

w = "This is the left side of..."
e = "a string with a right side."

print w + e #napise This is the left side of...a string with a right side.