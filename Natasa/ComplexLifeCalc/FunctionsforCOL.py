
#funkcija za gender
def calculate_gender(gender):
	if gender.lower() == "female" or gender.lower() == "f" or gender.lower() == "girl" or gender.lower() == "woman":
		return 100
	else:
		return 30

#funkcija za age
def calculate_age(age):
	if int(age) <= 10:
		return 10
	elif int(age) > 10 and int(age)<= 20:
		return 100
	elif int(age) > 20 and int(age) <= 35:
		return 20
	elif int(age) > 35 and int(age) <= 50:
		return 40
	else:
		return 0
#funkcija za status
def calculate_status(status):

	if status.lower() == "single":
		return 10
	elif status.lower() == "in a relationship" or status.lower() == "in relationship" or status.lower() == "relationship":
		return 20
	elif status.lower() == "in open relationship" or status.lower() == "in an open relationship" or status.lower() == "open relationship":
		return 40
	elif status.lower() == "it's complicated" or status.lower() == "complicated":
		return 80
	elif status.lower() == "i'm a pizza":
		return 90
	elif status.lower() == "it depends" or status.lower() == "depends":
		return 90
	else:
		return 100

#funkcija za ignorance
def calculate_ignorance(ignorance):
	if ignorance.lower() == "I live in a bubble" or ignorance.lower() == "bubble":
		return 0
	elif ignorance.lower() == "i'm aware" or ignorance.lower() == "i'm very aware" or ignorance.lower() == "aware" :
		return 100
	elif ignorance.lower == "somewhat aware" or ignorance.lower() == "so so" or ignorance.lower() == "meh":
		return 40
	else:
		return 80

def calculate_money(money_have):
	if int(money_have) < 5000:
		return 100
	elif int(money_have) >= 5000 and int(money_have) <= 10000:
		return 80
	elif int(money_have) >= 10000 and int(money_have) <= 50000:
		return 70
	elif int(money_have) >= 50000 and int(money_have) <= 150000:
		return 30
	else:
		return 0

def calculate_moneywant(money_wants):
	if int(money_wants) < 500:
		return 0
	else:
		if int(money_wants) < 3000:
			return 20
		elif int(money_wants) >= 3000 and int(money_wants) <= 15000:
			return 40
		elif int(money_wants) > 15000 and int(money_wants) <= 50000:
			return 60
		elif int(money_wants) > 50000 and int(money_wants) <= 150000:
			return 90
		else:
			return 100

def calculate_moneyspent(money_spent):
	if int(money_spent) < 2000:
		return  0
	elif int(money_spent) >= 2000 and int(money_spent) <= 10000:
		return  40
	elif int(money_spent) > 10000 and int(money_spent) <= 50000:
		return  80
	else:
		return  100

def calculate_popularity(online_popularity):
	if int(online_popularity) <= 10:
		return 0
	elif int(online_popularity) > 11 and int(online_popularity) <= 25:
		return 50
	elif int(online_popularity) > 25 and int(online_popularity) <= 45:
		return 75
	else:
		return 100

def calculate_friends(rl_friends):
	if int(rl_friends) < 3:
		return 0
	elif int(rl_friends) >=3 and int(rl_friends) <= 15:
		return 50
	else:
		return 100

#funkcija za izracun iz vec funkcij
def calculate_score(gender, age, status, ignorance, money_have, money_wants, money_spent, online_popularity, rl_friends):
	possibleperc = 900
	result = calculate_gender(gender) + calculate_age(age) + calculate_status(status) + calculate_ignorance(ignorance) + calculate_money(money_have) + calculate_moneywant(money_wants) + calculate_moneyspent(money_spent) + calculate_popularity(online_popularity) + calculate_friends(rl_friends)
	percent = float(result) / possibleperc * 100
	return percent

