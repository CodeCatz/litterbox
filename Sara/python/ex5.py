name = 'Sara Sabjan'
age = 22 # not a lie
height = 170 # cm
weight = 68 # kg
eyes = 'Blue'
teeth = 'Yellow'
hair = 'Brown'

print "Let's talk about %s." % name
print "She's %d cm tall." % height
print "She's %d kg heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % ( age, height, weight, age + height + weight) 
