print "Welcome to Body Mass Index calculator. Type 'Yes' to continue."

prompt = ">>>"

answer = raw_input(prompt) 
while answer != "Yes" and answer != "yes" and answer !="YES":
    answer = raw_input("Sorry, I didn't catch that. Enter again: ")

print "What is your weight?"
weight = raw_input(prompt)
while not weight.isdigit():
	weight = raw_input("Please type a number!")

print "What is your height in centimeters?"
height = raw_input(prompt)
while not height.isdigit():
	height = raw_input("Please type a number!")

BMI = int(weight) / ((int(height) * int(height))/100)

print "Your body mass index is %.2f" % BMI

BMI_prime = BMI / 25

print "Your prime body mass index is %.2f" % BMI_prime

if BMI > 25:
	print "You're too fat, chubby."
elif BMI < 18: 
	print "You're too skinny."
else:
	print "You're just right."