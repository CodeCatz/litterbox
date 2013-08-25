class my_song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def awesome_song(self):
		for line in self.lyrics:
			print line

euphoria = my_song(["Why, why can't this moment last forevermore?",
					"Tonight, tonight eternity's an open door",
					"No, don't ever stop doing the things you do",
					"Don't go, in every breath I take I'm breathing you"])

chorus = my_song(["Euphoria",
				"Forever, 'till the end of time",
				"From now on, only you and I",
				"We're going u-u-u-u-u-u-up",
				"Euphoria",
				"An everlasting piece of art",
				"A beating love within my heart",
				"We're going u-u-u-u-u-u-up"])

euphoria.awesome_song()

chorus.awesome_song()