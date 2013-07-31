# gender of subject
#   0 - male
#   1 - female
gender = 0

# age of subject
#   integer
age = 40

# Status of subject
#   0 - Single
#   1 - In a relationship
#   2 - In an open relationship
#   3 - It's complicated
#   4 - I'm a pizza
#   5 - Depends who's asking
status = 5

# how ignorant is the subject
# 0 - 100  percents
#   integer
ignorance = 10

# how much money does the subject have
#   float
money_have = 14662.00

# how much money does the subject want to have
#   float
money_wants = 20309.00

# how much money the subject spent
#   float
money_spent = 10991.00

# how popular is the subject online (cloudscore)
#   integer
popularity_online = 19

# number of subjects real life friends
#   integer
rl_friends = 7


# returns a sum of all variables... stupid as hell, but a placeholder for later
def sum_approach(gender, age, status, ignorance, money_have, money_wants, money_spent, popularity_online, rl_friends):
    return gender + age + status + ignorance + money_have + money_wants + money_spent + popularity_online + rl_friends


# returns a weighted sum... better, but still not perfect
def better_approach(gender, age, status, ignorance, money_have, money_wants, money_spent, popularity_online, rl_friends):
    weighted_sum = 0

    # if gender = male, 5 points more complicated
    if gender == 0:
        weighted_sum += 5

    # age weights
    if age < 10:
        weighted_sum += 0
    elif age < 20:
        weighted_sum += 4
    elif age < 35:
        weighted_sum += 2
    elif age < 50:
        weighted_sum += 4
    else:
        weighted_sum += 0

    # status weights
    status_weights = [0, 5, 9, 21, 3, 13]
    if weighted_sum >= 0 and weighted_sum < 6:
        weighted_sum += status_weights[status]
    else:
        # unknown status, adding a (random) default value
        weighted_sum += 7

    # calculate ignorance or something
    if ignorance >= 0 and ignorance <= 100:
        weighted_sum += (100 - ignorance) * 0.15
    else:
        # ignorance out of bounds, adding a (random) default value
        weighted_sum += 7

    # TODO: Add money calculation

    # online life complicates stuff
    weighted_sum += popularity_online / 3

    # more friends, ... not sure what
    if rl_friends > 15: # really? get real
        weighted_sum += 10 + rl_friends * 2
    if rl_friends > 8:
        weighted_sum += rl_friends - 8
    else:
        weighted_sum += 8 - rl_friends

    return weighted_sum




print "Simple (wrong) approaches:"
print "Sum of all values: ", sum_approach(gender, age, status, ignorance, money_have, money_wants, money_spent, popularity_online, rl_friends)
print "A better approach (weighted): ", better_approach(gender, age, status, ignorance, money_have, money_wants, money_spent, popularity_online, rl_friends)
