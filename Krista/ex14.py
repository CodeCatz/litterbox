from sys import argv

script, user_name = argv
prompt = '> ' # tole bo izpisal v vrstico kamor vnasamo podatke 

print "Hi %s, I'm the %s script." % (user_name, script) # %s je tista variabila, ki jo bomo vnesli - npr user_name = Krista,
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name # tle mu povemo kater vnos naj uporabi
likes = raw_input (prompt) # zapomni si kaj smo vnesli za variabilo "likes" + prompt 

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice
""" % (likes, lives, computer)
