#female = 1, male = 0
gender = 1

# 0-100 if age < 10 --> 0, 11 < age < 20 --> 4, 21 < age < 35 --> 2, 36 < age < 50 --> 4, 50+ --> 0

age = 25

result = 0

if (age > 11 and age  <= 20) or (age > 36 and age <= 50):
	result = result + 4

elif age > 20 and age <= 35:
	result = result + 2

else:
	result = result + 1


# 0 single, 1 relationship, 2 in open relationship, 3 it's complicated, 4 I'm a pizza, 5 depends
status = 4


# 0-100

ignorance = 22

if ignorance < 25:
	result = result + 0

elif ignorance < 70:
	result = result + 2

else:
	result = result + 5



# -5000 - 5000

money_have = 1000

if money_have < 0:
	result = result + 10

elif money_have == 0:
	result = result + 5

else:
	result += 1

# result = result + 1 je isto kot result += 1


# 0 - 5000
money_want = 1000

if money_want <= 2500:
	result += 1

else:
	result += 5



#0 - 5000
money_spent = 200

if money_spent <= 2500:
	result += 1

else:
	result += 2

#float 0-100.0
popularity_online = 50.0

if popularity_online <= 50:
	result += 3

else:
	result += 4

#0-20
rl_friends = 10

if rl_friends <=2:
	result += 5

elif rl_friends < 9:
	result += 1

else:
	result += 3

#0-10
children = 0

if children == 0:
	result += 1

elif children < 3:
	result += 2

else:
	result += 8

maximum = 18 + 23 + 104 + 5003 + 10142

my_value = age + status + ignorance + money_have + money_want + money_spent + popularity_online + rl_friends + children

# complexity = my score / maximum score * 100
print my_value / maximum * 100.0