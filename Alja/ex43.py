from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n----------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)



class Death(Scene):

	excuse = [
			"You're dead. what more do you want?",
			"Dead. Too bad.",
			"Dead and nobody comes to your funeral.",
			"Dead, cry me a river, will you?"
	]

	def enter(self):
		print Death.excuse[randint(0, len(self.excuse)-1)]
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print "'This is our ship, turn away!'"
		print "Looks like the alien is trying to protect something."
		print "'Hey, human, do you know why the ckicken crossed the street?'"
		answer = raw_input("> ")
		if answer == "to get to the other side":
			print "'Haha, that's so funny! I gotta tell mu buddies!'"
			print "And the alien leaves, well done."
			print "Go look into the big room at the end of the corridor"
			return 'laser_weapon_armory'
		else:
			return 'death'


class LaserWeaponArmory(Scene):

	def enter(self):
		print "It's an armory. You could use a bomb or two."
		print "Just unclock the keypad. You've got 10 guesses."

		code = "%d" % randint(1,9)
		guess = raw_input("Type a number between 1 and 9 >  ")

		guesses = 0

		while guess != code and guesses < 9:
			guesses += 1
			print "BZZZED %d!" %guesses
			guess = raw_input("Type a number between 1 and 9 >  ")

		if guess == code:
			print "Well done, here's your bomb. Go to the bridge."
			return 'the_bridge'
		else:
			print "Out of luck. You die."
			return 'death'

class TheBridge(Scene):

	def enter(self):
		print "Yeah, yeah, it's the bridge, place the bomb."
		print "Do you hurry or do you do it slowly?"

		action = raw_input("> ")

		if action == "hurry":
			print "Wrong choice."
			return 'death'
		elif action == "slowly":
			print "Good for you. The bridge blows off."
			return 'escape_pod'
		else:
			print "The aliens catch you."
			return 'death'

class EscapePod(Scene):

	def enter(self):
		print "Choose one of the pods, 1 to 5!"

		good_pod = randint(1,5)
		guess = raw_input("Which pod is it going to be? > ")

		if int(guess) != good_pod:
			print "Wrong choice"
			return 'death'
		else:
			print "Hurray, you made it!"
			return 'finished'

class Map(object):

	scenes = {
		'central_corridor' : CentralCorridor(),
		'laser_weapon_armory' : LaserWeaponArmory(),
		'the_bridge' : TheBridge(),
		'escape_pod' : EscapePod(),
		'death' : Death() 
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()

