# 1. del: funkcije

#gender: female = 5, male = 0

def calculate_score_for_gender(gender):
	if gender == "male":
		return 0
	else: return 5


#age: 0-100 if age < 10 --> 0, 11 < age < 20 --> 4, 21 < age < 35 --> 2, 36 < age < 50 --> 4, 50+ --> 1

def calculate_score_for_age(age):
	if (age > 11 and age  <= 20) or (age > 36 and age <= 50):
		return 4
	
	elif age > 20 and age <= 35:
		return 2
	
	elif age < 10:
		return 0

	else:
		return 1

#status: 0 = single, 1 = relationship, 2 = in open relationship, 3 = it's complicated, 4 = I'm a pizza, 5 = depends who's asking

def calculate_score_for_status(status):
	if status == "single":
		return 0

	elif status == "in a relationship":
		return 1

	elif status == "in an open relationship":
		return 2

	elif status == "it's complicated":
		return 3

	elif status == "I'm a pizza":
		return 4

	else:
		return 5


# ignorance: 0 = Problem is my challenge, 1 = Who gives a fuck, 2 = I'm an angel

def calculate_score_for_ignorance(ignorance):
	if ignorance == "problem is my challenge":
		return 0

	elif ignorance == "who gives a fuck":
		return 1

	else:
		return 2


# money_have: -10000+ = 6, (-10000)-(-5000) = 5, -5000-0 = 4, 0-500 = 3, 500-3000 = 2, 3000-10000 = 1, 10000+ = 0

def calculate_score_for_money_have(money_have):
	if money_have <= (-10000.0):
		return 6.0

	elif money_have > (-10000.0) and money_have <= (-5000.0):
		return 5.0

	elif money_have > (-5000.0) and money_have <= 0.0:
		return 4.0

	elif money_have > 0.0 and money_have <= 500.0:
		return 3.0

	elif money_have > 500.0 and money_have <= 3000.0:
		return 2.0

	else:
		return 0.0

# ---ZAKAJ MI NE PREPOZNA POZITIVNIH FLOATING NUMBERS IN NOBENE NEGATIVE (INTEGER ALI FLOATING NEGATIVNE) KOT STEVILKO?
# -->PRED RAW INPUT MORAS DAT FLOAT, CE NI CELA STEVILKA IN ODSTRANI .ISDIGIT, KER .ISDIGIT JE LE ZA CELE STEVILKE!


# money_want: 0 = 0, 0-1000 = 1, 1000-5000 = 3, 5000-10000 = 4, 10000+ = 5

def caluculate_score_for_money_want(money_want):
	if money_want == 0:
		return 0

	elif money_want > 0.0 and money_want <= 1000.0:
		return 1

	elif money_want > 1000.0 and money_want <= 5000.0:
		return 3

	elif money_want > 5000.0 and money_want <= 10000.0:
		return 4

	else:
		return 5



# 2. del: sestevek funkcij

def calculate_score(gender, age, status, ignorance, money_have, money_want):
	result = calculate_score_for_gender(gender)
	result += calculate_score_for_age(age)
	result += calculate_score_for_status(status)
	result += calculate_score_for_ignorance(ignorance)
	result += calculate_score_for_money_have(money_have)
	result += caluculate_score_for_money_want(money_want)
	return result


# 3. del: ------------- output za userja

#gender
print "Are you male or female?"
gender = raw_input(">> ")
#note to self: "while" pomeni da cekira na loop, "if" cekira enkratno
while (gender != "male") and (gender != "female"):
	gender = raw_input("Check your gender again: ")

#age
print "How old are you?"
age = raw_input(">> ")
while not age.isdigit():
	age = raw_input("Admit it, you're old. Now write your real age: ")

#status
print "What is your marital status?"
status = raw_input(">> ")
while (status != "single") and (status != "in a relationship") and (status != "in an open relationship") and (status != "it's complicated") and (status != "I'm a pizza"):
	status = raw_input("Yeah, right... Think again: ")

#ignorance
print "How ignorant are you?"
ignorance = raw_input(">> ")
while (ignorance != "problem is my challenge") and (ignorance != "who gives a fuck") and (ignorance != "I'm an angel"):
	ignorance = raw_input("You can't be that ignorant. Try again: ")

#money_have
print "How much money have you got?"
money_have = float(raw_input(">> "))
while not money_have:
	money_have = float(raw_input("We aren't tax collectors, so be honest: "))
# PRED RAW INPUT MORAS DAT FLOAT, CE NI CELA STEVILKA IN ODSTRANI .ISDIGIT, KER .ISDIGIT JE LE ZA CELE STEVILKE!

#money_want
print "In addition to the money you've got, how much money do you want to have?"
money_want = float(raw_input(">> "))
while money_want < 0: #---->zato, da je pozitivno stevilo!
	money_want = float(raw_input("I didn't ask for apples and peaches. So, how much money do you want? "))

# 4.del: sestevek

print "Kompliciranost tvojega zivljenja je: ", calculate_score(gender, int(age), status, ignorance, money_have, money_want)


