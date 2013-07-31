from sys import exit
from random import choice

cats = []

cuteness = ['look at those big eyes',
			 'listen to that sweet purr',
			 'imagine the softness of that belly',
			 'feel the softness of its fur',
			 'look at that bushy tail',
			 'its mom got ran over by a car',
			 'it is all alone in this world',
			 'it just needs a little love',
			 'look at those furry paws',
			 'look at the cute ear tufts']

def game_over(why):
	print "You lose.", why
	exit(0)

def start():
	print "*** WELCOME TO THE CRAZY CAT LADY GAME! ***\n"
	print "You wake up, in the middle of the night."
	print "There's a faint meowing coming from underneat your bed."
	print "Do you check for kittens or go back to sleep?"

	next = raw_input("> ")

	if "check" in next:
		print "There's a little scared kitten under the bed!"
		new_kitten()
	elif "sleep" in next:
		game_over("How is sleep more important than kittens?")
	else:
		game_over("Try to keep up with instructions next time.")

def new_kitten():
	print "Do you keep it or give it away?"

	next = raw_input("> ")

	if "keep" or "Keep" or "KEEP" in next:
		print "That's right. Cats are awesome."
		setup_cat()
	elif len(cats) > 0:
		print "But %s. Let's try this again.\n" % choice(cuteness)
		new_kitten()
	else:
		game_over("You selfish bastard. Don't tell me you like dogs better than cats?")


def setup_cat():
	print "\nAll right, new cat in the family."
	print "What will you call it?"

	name = raw_input("> ")

	cats.append(name)

	print "Well done, you've got a cat named %s" % name
	
	if len(cats) > 1:
		print "Now it's you and %d cats: " % len(cats)

		for cat in cats:
			print cat

		if len(cats) == 7:
			cat_domination()

	print "\nOh look, %s has a cat friend! It's so cute!" % name
	new_kitten()


def cat_domination():
	print "\nThe cats take over the world."
	print "All humans are enslaved."
	print "As a form of gratitude, you stay on litterbox duty forever."
	print "But other than that you're absolutely free to pet the cats"
	print "and bathe in their beauty."
	print "\nCONGRATS, you win the CRAZY CAT LADY trophy!"
	exit(0)

print start()

