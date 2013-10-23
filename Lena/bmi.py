print "What is your weight?",
weight = int(raw_input())
print "What is your height in meters?",
height = float(raw_input())

BMI = weight / (height * height)

print "Your body mass index is %.2f" % BMI

BMI_prime = BMI / 25

print "Your prime body mass index is %.2f" % BMI_prime

if BMI > 25:
	print "You're too fat, chubby."
if BMI < 18: 
	print "You're too skinny."
if BMI > 18 and BMI < 25: 
	print "You're just right."