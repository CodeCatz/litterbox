print "______________________________________________________"
print "***WELCOME TO COMPLEXITY OF LIFE CALCULATOR !*** "
print """We'll need you to answer a few questions, which will then in return determine,
how complex your life is!"""
print "______________________________________________________"

prompt = "***> "

#NAME (anything goes)

print ">Exciting right? Now, lets get started! What's your name?"
name = raw_input(prompt)
if name.isalpha() == True:
	print "Arr %s, welcome aboard!" %name
else:
	print "That's not a name... That's not a name. * sang by computerized voice in the 'That's not my name' song melody*",
	print "Try again!"
	name = raw_input(prompt)
#Loop bi tukej prov prisel samo ga se ne znam :D Coming soon torej.

#GENDER (female/male) CHECKED FOR BUGS

print">What is your gender?"
gender = raw_input (prompt)

if gender.lower() == "female" or gender.lower() == "f" or gender.lower() == "girl" or gender.lower() == "woman":
	genderperc = 100
	print """For a %s, life is full of boring stuff, waiting on someone to make them complicated!
Like this script for example.""" %gender
else:
	print "Phew! Not being a female already reduces your risk of high life complexity. Well, unless you're dating one."
	genderperc= 30

#AGE (each age gives a certain level of complexity) - CHECKED FOR BUGS

print ">How old are you? Your real age...no cheating here!"
age = raw_input(prompt)

if int(age) <= 10:
	ageperc = 10
elif int(age) > 10 and int(age)<= 20 :
	ageperc = 100
elif int(age) > 20 and int(age) <= 35:
	ageperc = 20
elif int(age) > 35 and int(age) <= 50:
	ageperc = 40
else:
	ageperc = 0

#STATUS - CHECKED FOR BUGS

print ">So, let's get more intimate. How would you define your relationship status?"
status = raw_input(prompt)
# 0 - single, 1 - in a relationship ,2 - in open relationship, 3 - it's complicated, 4 - I'm a pizza, 5 - depends
if status.lower() == "single":
	print "Whoop, whoop! *wink wink*. No you're not imagining it... computer is flirting with you!"
	statusperc = 10
elif status.lower() == "in a relationship" or status.lower() == "in relationship" or status.lower() == "relationship":
	print "Boring! Good thing about being boring though, is that it's not that complicated...yet!"
	statusperc = 20
elif status.lower() == "in open relationship" or status.lower() == "in an open relationship" or status.lower() == "open relationship":
	print "Oh you swinger, you."
	statusperc = 40
elif status.lower() == "it's complicated" or status.lower() == "complicated":
	print "That just pumped up your complexity of life score by a lot!"
	statusperc = 80
elif status.lower() == "i'm a pizza":
	print "NOM NOM... You've just been eaten!"
	statusperc = 90
elif status.lower() == "it depends" or status.lower() == "depends":
	print "What does that even mean? This is more complicated than the 'it's complicated' status!"
	statusperc = 90
else:
	statusperc = 100


#IGNORANCE

print ">Are you aware of the world around you or do you live in a bubble?"
ignorance = raw_input(prompt)
if ignorance.lower() == "I live in a bubble" or ignorance.lower() == "bubble":
	ignoranceperc = 0
	print "Well they do say that Ignorance is a bliss. You must be a very happy person!"
elif ignorance.lower() == "i'm aware" or ignorance.lower() == "i'm very aware" or ignorance.lower() == "aware" :
	print "Well done, you must be a smart person! Sadly for you that also increases your complexity of life score."
	ignoranceperc = 100
elif ignorance.lower == "somewhat aware" or ignorance.lower() == "so so" or ignorance.lower() == "meh":
	ignoranceperc = 40
else:
	print "Ooops! Your answer is too philosophical for me."
	print "Just give me a number between 0 and 100, where 100 makes you \n 'well aware' and 0 makes you a 'bubblehead'"
	ignoranceperc = raw_input(prompt)

# MONEY THAT WE HAVE

print ">How much money do you have?"
money_have = raw_input(prompt)

if int(money_have) < 5000:
	moneyperc = 100
elif int(money_have) >= 5000 and int(money_have) <= 10000:
	moneyperc = 80
elif int(money_have) >= 10000 and int(money_have) <= 50000:
	moneyperc = 70
elif int(money_have) >= 50000 and int(money_have) <= 150000:
	moneyperc = 30
else:
	moneyperc = 0

# MONEY WE WANT
print ">How much money you feel you need?"
money_wants = raw_input(prompt)
if int(money_wants) <= int(money_have) :
	print "Well aren't you lucky !"
	moneywantperc = 0
else:
	if int(money_wants) < 3000:
		print "Well, arn't you a humble bee!"
		moneywantperc = 20
	elif int(money_wants) >= 3000 and int(money_wants) <= 15000:
		moneywantperc = 40
	elif int(money_wants) > 15000 and int(money_wants) <= 50000:
		moneywantperc = 60
	elif int(money_wants) > 50000 and int(money_wants) <= 150000:
		print "the more the merrier huh?"
		moneywantperc = 90
	else:
		print "the more the merrier huh :D ?"
		moneywantperc = 100



# MONEY WE SPENT
print ">How much money did you spend this year?"
money_spent = raw_input(prompt)
if int(money_spent) < 2000:
	moneyspentperc = 0
	print "Well, getting that new MacBook was totally worth it!"
elif int(money_spent) >= 2000 and int(money_spent) <= 10000:
	moneyspentperc = 40
elif int(money_spent) > 10000 and int(money_spent) <= 50000:
	moneyspentperc = 80
	print "Gees! Did you invest in one of those pyramid scheme Multi level marketing scams or something?"
else:
	moneyspentperc = 100

# ONLINE POPULARITY
print ">What's your Klout score?"
popularity_online = raw_input(prompt)
if input > 0

	elif int(popularity_online) <= 10:
		popularityperc = 0
		print "You don't appear to be popular. On the bright side, this reduces  human relationships related complications."
	elif int(popularity_online) > 11 and int(popularity_online) <= 25:
		popularityperc = 50
	elif int(popularity_online) > 25 and int(popularity_online) <= 45:
		popularityperc = 75
	else:
		popularityperc = 100
		print "Guess you're an Internet personality of some sort? "
else:
	print "error!"

# REAL LIFE POPULARITY
print ">How many real life friends do you have?"
rl_friends = raw_input(prompt)
if int(rl_friends) < 3:
	rl_friendsperc = 0
	print "You don't seem to have a lot of friends - good thing though is, that it reduces your human relationships related complications."
elif int(rl_friends) >=3 and int(rl_friends) <= 15:
	rl_friendsperc =50
else:
	print "Pretty popular! "
	rl_friendsperc = 100


#SUM IT UP
possibleperc = 900
result = int(genderperc)+ int(statusperc)+ int(ageperc) + int(ignoranceperc) + int(moneyperc)+ int(moneywantperc )+ int(moneyspentperc) + int(popularityperc) + int(rl_friendsperc)
percent = float(result) / possibleperc * 100


print "____________________________________________________________"
print """Your name is %s. You are a %s, %d old, your relationship status is %s and you consider your ignorance level as: %s.
You have %d EUR but you wish you had %d EUR. You would probably get there sooner if you didn't spend %d EUR this year.
"""%(name, gender, int(age), status, ignorance, int(money_have), int(money_wants), int(money_spent))
print "Your popularity level based on Klout score is %d and you only have %d real life friends"%(int(popularity_online), int(rl_friends))
print "*** ______________________________________________________***"
print "   CONGRATULATIONS, YOUR LIFE IS %d PERCENT COMPLICATED!" %float(percent)
print "*** ______________________________________________________***"