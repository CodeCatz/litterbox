print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear doesn't mind sharing the cake. He's lonely and wants you to stay with him. Do you..."
		print "1 Move in with the bear."
		print "2 Try to run away."
		print "3 Finish the cake before answering."

		proposal = raw_input("> ")

		if proposal == "1":
			print "That's so nice of you. Congratulations on your wedding!"
		elif proposal == "2":
			print "The bear eats you whole. He doens't like rejection."
		elif proposal == "3":
			print "Good choice, it was a great cake. Now what?"
			print "1 Ask for more cake."
			print "2 Try to run away."
			print "3 Stay with the bear"

			end_cake = raw_input("> ")

			if end_cake == "1":
				print "The bear doesn't have any. He'll get you another one. He leaves the room and you..."
				print "1 Sneak out without leaving a note."
				print "2 Sneak out and leave the note \"It's not you, it's me. You deserve better.\""
				print "3 Decide to stay and wait for more cake."

				alone = raw_input("> ")

				if alone == "1":
					print "Good for you, you're free. But the bear eventually tracks you and eats you whole. Never leave without a note."
				elif alone == "2":
					print "Hurray, you're free! After a while the bear sends you a wedding photo and a note: \"Thanks, I did find somebody better!\""
				elif alone == "3":
					print "The bear makes you eat the whole cake. Your tummy explodes."
				else:
					print "The bear eats you, because you're not following the game."

			elif end_cake == "2":
				print "The bear eats you whole. He doens't like rejection."
			elif end_cake == "3":
				print "Good for you. You marry the bear, but have enough cake for the rest of your life. Not bad."
			else:
				print "Trying to trick me, are you? Well, %s doesn't please the bear and you're cooked alive. Game over."
		else:
			print "%s wasn't a smart choice. The bear cooks you alive."


	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"