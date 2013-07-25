# 0 - 100
age = 29

# male = 1, female 10
gender = 10

# 2 single, 4 relationship,  6 open relationship, 8 it's complicated, 10 I'm a pizza, 0 depends
status = 4

# 0 - 10 (%)
ignorance = 1

# euros
money_have = 1000
money_wants = 10
money_spent = -200

money = (money_have - money_spent) - money_wants

def money_score(money):
	if money == 0:
		return 2
	elif money > 0:
		return 0
	elif money < 0 and money >= -1000:
		return 5
	else:
		return 10


# klout score
popularity_online = 64

# number of real friends
# 0 - 2 = 0, 3 - 5 = 4, 6+ = 10
rl_friends = 0


def age_calc(age):
	if age <= 10:
		return 2
	elif age >= 11 and age <= 20:
		return 8
	elif age >= 21 and age <= 30:
		return 4
	elif age >= 31 and age <= 50:
		return 10
	elif age >= 51:
		return 0
	else:
		return 0

def klout_calc(score):
	if score <= 40:
		return 0
	elif score > 40 and score <= 50:
		return 4
	elif score > 50 and score <= 60:
		return 6
	elif score > 60 and score <= 80:
		return 8
	elif score > 80:
		return 10
	else:
		return 0

my_score = age_calc(age) + gender + status - ignorance + money_score(money) + klout_calc(popularity_online) + rl_friends
max_score = 10 * 6

print "Your complexity score is:"
print (my_score / float(max_score)) * 100