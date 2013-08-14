age = 40
gender = 0

def calculate_score_for_gender(gender):
	if gender == 0:
		return 10
	else:
		return 5

def calculate_score_for_age(age):
	return age * 2

def calculate_score(gender, age):
	result = calculate_score_for_gender(gender)
	result += calculate_score_for_age(age)
	return result

print "Kompliciranost je: ", calculate_score(gender, age)