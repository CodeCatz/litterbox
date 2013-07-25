prompt = "***>"
print "________________________________________________________________________"
print "***WELCOME TO COMPLEXITY OF LIFE CALCULATOR !*** "
print "We'll need you to answer a few questions, which will then determine how complex your life is!"
print "________________________________________________________________________"
#NAME (anything goes)

print "Exciting right? Now, lets get started! What's your name?"
name = raw_input(prompt)
if name.isalpha() == True:
	print "Arr %s, welcome aboard!" %name
else:
	print "That's not a name... That's not a name. *sings it in the 'That's not my name' song melody*",
	print "Try again!"
	name = raw_input(prompt)


#GENDER (female/male)

print"What is your gender?"
gender = raw_input (prompt)

if gender.lower() == "female" or gender.lower() == "f" or gender.lower() == "girl" or gender.lower() == "woman":
	genderperc = 100
	print "Life is full of boring stuff  waiting  on someone to make them complicated! ",
	print "Like this script for example."
else:
	print "Phew! Not being a female already reduces your risk of high life complexity. Well, unless you're dating them."
	genderperc= 30

#STATUS

print "So, let's get more intimate. How would you define your relationship status?"
status = raw_input(prompt)
# 0 - single, 1 - in a relationship ,2 - in open relationship, 3 - it's complicated, 4 - I'm a pizza, 5 - depends
if status.lower() == "single":
	print "Whoop whoop! *wink wink* Yes you're not imagining it... computer is flirting with you!"
	statusperc = 10
elif status.lower() == "in a relationship" or status.lower() == "in relationship" or status.lower() == "relationship":
	print "Boring! Good thing about being boring is less drama. For now!"
	statusperc = 20
elif status.lower() == "in open relationship":
	print "Oh you swingers, you."
	statusperc = 30
elif status.lower() == "it's complicated" or status.lower() == "complicated":
	print "That just pumped up your complexity of life score!"
	statusperc = 50
elif status.lower() == "i'm a pizza":
	print "NOM NOM... You've just been eaten!"
	statusperc = 90
elif status.lower() == "it depends" or status.lower() == "depends":
	print "What does that even mean? This is more complicated than the 'it's complicated' relationships!"
	statusperc = 80
else:
	statusperc = 100

# #AGE (each age gives a certain level of complexity)

print "How old are you? Real age...no lying!"
age = raw_input(prompt)

if age <= 10:
	ageperc = 20
elif age<= 20 and age >= 11:
	ageperc = 100
elif age > 21 and age <= 35:
	ageperc = 20
elif age >= 36 and age <= 50:
	ageperc = 10
else:
	ageperc = 0

#IGNORANCE 

print "Are you aware of the world around you or do you live in a bubble?"
ignorance = raw_input(prompt)
if ignorance.lower() == "I live in a bubble" or ignorance.lower() == "bubble":
	ignoranceperc = 0
	print "Well they do say that Ignorance is a bliss...You're probably a very happy person."
elif ignorance.lower() == "I'm aware" or ignorance.lower() == "I'm very aware" or ignorance.lower() == "aware":
	print "Good job! Sadly for you that also increases your complexity of life score."
	ignoranceperc = 100
elif ignorance.lower == "somewhat aware" or ignorance.lower() == "so so":
	ignoranceperc = 40
else:
	print "Ooops! Your answer seems to be invalid"
	print "Just give us a number between 0 and 100, where 0 means \n 'completely aware' and 100 makes you a 'bubblehead'"
	ignoranceperc = raw_input(prompt)

# MONEY THAT WE HAVE

print "How much money do you have?"
money_have = raw_input(prompt)

if money_have < 5000:
	moneyperc = 70
elif money_have >= 5000 and money_have <= 10000:
	moneyperc = 50
elif money_have >= 10000 and money_have <= 50000:
	moneyperc = 30
elif money_have >= 50000 and money_have <= 150000:
	moneyperc = 20
else:
	moneyperc = 0

# MONEY WE WANT
print "How much money you feel you need?"
money_wants = raw_input(prompt)
if money_wants <= money_have :
	print "Well arn't you lucky !"
	moneywantperc = 0
else:
	if money_wants < 3000:
		print "Well, arn't you a humble bee!"
		moneywantperc = 20
	if money_wants >= 3000 and money_wants <= 15000:
		moneywantperc = 40
	if money_wants > 15000 and money_wants <= 50000:
		moneywantperc = 60
	if money_wants > 50000 and money_wants <= 150000:
		moneywantperc = 90
	else: 
		moneywantperc = 100


# MONEY WE SPENT
print "How much money did you spend in your adult life?"
money_spent = raw_input(prompt)
if money_spent < 1000:
	moneyspentperc = 0
if money_spent >= 1000 and money_spent <= 10000:
	moneyspentperc = 40
if money_spent > 10000 and money_spent <= 50000:
	moneyspentperc = 80
else:
	moneyspentperc = 100

# ONLINE POPULARITY
print "What's your Klaut score?"
popularity_online = raw_input(prompt)

# REAL LIFE POPULARITY
print "How many real life friends do you have?"
rl_friends = raw_input(prompt)

#SUM IT UP
sumdefault = 900
sum = genderperc+ statusperc + ageperc+ ignoranceperc + moneyperc +int(moneywantperc) + int(moneyspentperc) + int(popularity_online) + int(rl_friends)

percent = float(sum)/float(sumdefault)*100


print """Your name is %s. You are a %s, %d old, your relationship status is %s and you consider your ignorance level as: %s. You have %d amount of money but you wish you had %f EUR.. You would probably
You would probably get there sooner if you didn' spend %f eur so far.
"""%(name, gender, int(age), status, ignorance, int(money_have), int(money_wants), int(money_spent))
print "Your popularity level based on Klaut score is %d and you only have %d of real life friends"%(int(popularity_online), int(rl_friends))
print "*** ________________________________________________________________________"
print "Congratulations, your life is %d percent complicated" %percent
print "*** ________________________________________________________________________"