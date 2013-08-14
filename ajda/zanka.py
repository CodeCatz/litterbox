pogoj = False
age = raw_input("vpisi starost: ")
while not pogoj:
	if not age.isdigit():
		print "Vpisi samo stevilke!"
	elif int(age) < 3:
		print "Ne verjamem."
	elif int(age) > 150:
		print "Ha!"
	else: pogoj = True

	if not pogoj:
		age = raw_input("Se enkrat vpisi starost: ")

#je isto kot:

pogoj = True
age = raw_input("vpisi starost: ")
while pogoj:
	if not age.isdigit():
		print "Vpisi samo stevilke!"
	elif int(age) < 3:
		print "Ne verjamem."
	elif int(age) > 150:
		print "Ha!"
	else: pogoj = False

	if pogoj:
		age = raw_input("Se enkrat vpisi starost: ")