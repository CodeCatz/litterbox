def calculate_score_for_gender(gender):
    if gender == "male":
        return 10
    else:
        return 5

def calculate_score_for_age(age):
    return age * 2

def calculate_score(gender, age):
    result = calculate_score_for_gender(gender)
    result += calculate_score_for_age(age)
    return result