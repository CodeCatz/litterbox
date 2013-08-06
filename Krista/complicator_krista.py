result = 0
# male = 0, female = 1
gender = 1
#0-100
#if age <10=0, <11 age 20 = 4, <21 age 35 = 2, <36 age 50 = 4, >50=1,
age = 2

if (age > 11 and age <= 20) or (age > 36 and age <= 50):
	result = result + 4

elif age > 20 and age <= 35:
	result = result + 2

else:
    result = result + 1

status = 5


ignorance = 50

if ignorance < 20:
    result = result + 1
elif ignorance < 40:
	result = result + 2
elif ignorance < 60:
	result += 3
elif ignorance < 80:
	result += 4

# -5000 - 5000
money_have = 1000

if money_have < -3000:
    result += 5
elif money_have < 0:
	result += 4
elif money_have < 3000:
     result += 3
elif money_have < 5000:
	result += 2

# 0 - 5000
money_want = 2000


if money_want < 2500:
	result += 4
elif money_want < 5000:
    result += 8

#0 - 5000
money_spent = 800




popularity_online = 88
rl_friends = 13
children = 0

print age + status + ignorance + money_spent + money_want + money_have + popularity_online + rl_friends + gender + children

maximum = 1 + 4 + 5 + 100 + 5000 + 5000 + 5000 + 100.0 + 50 + 10

my_valute = gender + age + ignorance + money_have + money_want + money_spent + popularity_online + rl_friends + children

print result
