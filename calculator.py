print "                                              "
print """WELCOME TO THE COMPLEXITY OF LIFE CALCULATOR! 
You'll be asked some simple questions and depending on your answers the calculator will deduct how much complicated your life is.
So if you're ready, let's get started! :)
"""

prompt = ">>> "

print "Please type in YES to continue. "
answer = raw_input(prompt) 
while answer != "Yes" and answer != "yes" and answer !="YES":
    answer = raw_input("Sorry, I didn't catch that. Enter again: ") 

print "Let's start off with the basic questions. What's your name?"
name = raw_input(prompt)

print "Welcome %r. \nPlease type in your gender. " % name #male - 50 , female - 100
gender = raw_input(prompt)
while gender != "male" and gender != "Male" and gender!= "MALE" and gender != "m" and gender != "female" and gender != "Female" and gender != "FEMALE" and gender != "f":
	gender = raw_input("Sorry, please choose either male or female. ")


print "How old are you? " #0-100
age = raw_input(prompt)
while not age.isdigit():
	age = raw_input("Please type a number between 0 and 150. ")



print "How would you define your relationship status?:  \n0 - single, \n1 - in relationship, \n2 - in open relationship, \n3 - it's complicated, \n4 - I'm a pizza, \n5 - depends \n"
status = raw_input(prompt)
while not status.isdigit():
	status = raw_input("Please type in a number shown before the listed statuses above. ")



print "How ignorant of the world are you? Type a number between 0 and 100 (0 meaning 'stressing yourself over every little thing' and 100 meaning 'I don't give a shit'): " #0-100
ignorance = raw_input(prompt)
while not ignorance.isdigit():
	ignorance = raw_input("Please type a number between 0 and 100: ")


print "How much money do you have (in Euros)? Type a number: " #integers (cela stevila)
money_have = raw_input(prompt)
while not money_have.isdigit():
	money_have = raw_input("Please type a number: ")

print "How much money do you want (in Euros)? Type a number: " #integers
money_wants = raw_input(prompt)
while not money_wants.isdigit():
	money_wants = raw_input("Please type a number: ")


print "Now let's see how popular are you. :P How many friends do you have on Facebook? " #klout score
popularity_online = raw_input(prompt)
while not popularity_online.isdigit():
	popularity_online = raw_input("Please type a number: ")


print "How many friends do you have in real life? " #integer 0 - ~ 
rl_friends = raw_input(prompt)
while not rl_friends.isdigit():
	rl_friends = raw_input("Please type a number: ")




if gender.lower() == "male" or gender.lower() == "m":   
	gender_result = 1
elif gender.lower() == "female" or gender.lower() == "f":
   gender_result = 1
#else:
	#result = result + 0



if int(age) <= 10:
	age_result = 0
elif (int(age) > 10 and int(age) <= 20) or (int(age) > 35 and int(age) <= 50):    
	age_result = 4
elif int(age) > 20 and int(age) <= 35:
	age_result = 2
else: 
	age_result = 1


status_result = 0
status_result += int(status)


if int(ignorance) <= 20:
	ignorance_result = 1
elif int(ignorance) > 20 and int(ignorance) <= 40:
	ignorance_result = 2
elif int(ignorance) > 40 and int(ignorance) <= 60:
	ignorance_result = 3
elif int(ignorance) > 60 and int(ignorance) <= 80:
	ignorance_result = 4
else:
	ignorance_result = 5


if int(money_have) <= 0:
	money_have_result = 0
elif int(money_have) > 0 and int(money_have) <= 200:
	money_have_result = 1
elif int(money_have) > 200 and int(money_have) <= 500:
    money_have_result = 2
elif int(money_have) > 500 and int(money_have) <= 1200:
	money_have_result = 3
elif int(money_have) > 1200 and int(money_have) <= 2400:
	money_have_result = 4
elif int(money_have) > 2400 and int(money_have) <= 5000:
	money_have_result = 5
else: 
	money_have_result = 6


if money_wants <= 100:
	money_wants_result = 5
elif money_wants > 100 and money_wants <= 500:
	money_wants_result = 4
elif money_wants > 500 and money_wants <= 1000:
	money_wants_result = 3
elif money_wants > 1000 and money_wants <= 5000:
	money_wants_result = 2
elif money_wants > 5000 and money_wants <= 10000:
	money_wants_result = 1
else:
	money_wants_result = 0

if popularity_online <= 50:
	popularity_online_result = 0
elif popularity_online > 50 and popularity_online <= 100:
	popularity_online_result = 1
elif popularity_online > 100 and popularity_online <= 200:
	popularity_online_result = 2
elif popularity_online > 200 and popularity_online <= 300:
	popularity_online_result = 3
elif popularity_online > 300 and popularity_online <= 400:
	popularity_online_result = 4
else:
	popularity_online_result = 5

if rl_friends <= 10:
    rl_friends_result = 4
elif rl_friends > 10 and rl_friends <= 20:
	rl_friends_result = 5
elif rl_friends > 20 and rl_friends <= 30:
    rl_friends_result = 3
elif rl_friends > 30 and rl_friends <= 40:
	rl_friends_result = 2
elif rl_friends > 40 and rl_friends <= 50:
	rrl_friends_result = 1
else:
	rl_friends_result = 0


total = gender_result * 0.02 + age_result * 0.06 + status_result * 0.1 + ignorance_result * 0.17 + money_have_result * 0.13 + money_wants_result * 0.13 + popularity_online_result * 0.14 + rl_friends_result * 0.25


complexity = (total/ 4.99) * 100 

if complexity <= 30.00:
	print """
Oh no, only %r %% %r. Your life is very complicated. You should take some time off to cool your head. """ % (int(complexity), name)
elif complexity > 30.00 and complexity <= 47.00:
	print """
Your score is only %r %% %r. You should take it easy for a while. """ % (int(complexity), name)
elif complexity > 47.00 and complexity <= 60.00:
	print """
Your score is %r %% %r. Not bad. Not bad. Right somewhere in the middle. Although taking a vacation once in a while wouldn't be such a bad idea. ;) """ % (int(complexity), name)
elif complexity > 60.00 and complexity <= 80.00:
	print """
Wow, your score is %r %% %r. I must say you're living a decent life. :) """ % (int(complexity), name)
elif complexity > 80.00 and complexity <= 100.00:
	print """
Congratulations!!! Your score is %r %% %r. Keep it up! :D""" % (int(complexity), name)



