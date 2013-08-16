def gender_calc(gender):
	if gender == "male":
		return 1
	elif gender == "female":
		return 1

def age_calc(age):
	if age <= 10:
		return 1
	elif age > 10 and age <= 20:
		return 2
	elif age > 20 and age <= 30:
		return 3
	elif age > 31 and age <= 50:
		return 4
	elif age > 50:
		return 5
	else:
		return 0

def status_calc(status):
	if status == "1":
		return 1
	elif status == "2":
		return 2
	elif status == "3":
		return 3
	elif status == "4":
		return 4
	elif status == "5":
		return 5
	elif status == "6":
		return 6

def ignorance_calc(ignorance):
	if ignorance <= 20:
		return 1
	elif ignorance > 20 and ignorance <= 40:
		return 2
	elif ignorance > 40 and ignorance <= 60:
		return 3
	elif ignorance > 60 and ignorance <= 80:
		return 4
	else: 
		return 5

def money_have_calc(money_have):
	if money_have <= 0:
		return 0
	elif money_have > 0 and money_have <= 200:
		return 1
	elif money_have > 200 and money_have <= 500:
		return 2
	elif money_have > 500 and money_have <= 1200:
		return 3
	elif money_have > 1200 and money_have <= 2400:
		return 4
	elif money_have > 2400 and money_have <= 5000:
		return 5
	else: 
		return 6

def money_wants_calc(money_wants):
	if money_wants <= 100:
		return 5
	elif money_wants > 100 and money_wants <= 500:
		return 4
	elif money_wants > 500 and money_wants <= 1000:
		return 3
	elif money_wants > 1000 and money_wants <= 5000:
		return 2
	elif money_wants > 5000 and money_wants <= 10000:
		return 1
	else:
		return 0

def popularity_online_calc(popularity_online):
	if popularity_online <= 50:
		return 0
	elif popularity_online > 50 and popularity_online <= 100:
		return 1
	elif popularity_online > 100 and popularity_online <= 200:
		return 2
	elif popularity_online > 200 and popularity_online <= 300:
		return 3
	elif popularity_online > 300 and popularity_online <= 400:
		return 4
	else:
		return 5

def rl_friends_calc(rl_friends):
	if rl_friends <= 10:
		return 4
	elif rl_friends > 10 and rl_friends <= 20:
		return 5
	elif rl_friends > 20 and rl_friends <= 30:
		return 3
	elif rl_friends > 30 and rl_friends <= 40:
		return 2
	elif rl_friends > 40 and rl_friends <= 50:
		return 1
	else:
		return 0


def total_calc(gender, age, status, ignorance, money_have, money_wants, popularity_online, rl_friends):
	total_calc = gender_calc(gender) * 0.02 + age_calc(age) * 0.06 + status_calc(status) * 0.1 + ignorance_calc(ignorance) * 0.17 + money_have_calc(money_have) * 0.13 + money_wants_calc(money_wants) * 0.13 + popularity_online_calc(popularity_online) * 0.14 + rl_friends_calc(rl_friends) * 0.25
	return total_calc



def complexity_calc(complexity):
	complexity = (total_calc/ 5.15) * 100
	return complexity

	