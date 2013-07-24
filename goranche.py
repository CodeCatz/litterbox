# 
# Exercises from http://learnpythonthehardway.org
#

print
# Exercise 1
print "Really? :)"
print "I'm not writing a hello world, am I?"
print 'No way!!! Where\'s the link to the next exercise?'
print 'Oh, right, "double quotes" in print; next, please'


print
# Exercise 2
print "I think my previous code shows that I know about comments"

print
# Exercise 3
print "I have no chicken, I'll count something else"
print "Number of visible stars", 272 * 11 + 8
print "Yup, python math is the same as pretty much all other math"

print
# Exercise 4
visible_stars = 6000
hemispheres = 2
visible_rural = 2000
visible_urban = 20
print "There are about", visible_stars, "stars visible to the unaided eye"
print "Only half of those, ", visible_stars / hemispheres, "are visible from a single point at any time"
print visible_rural, "will be visible at sea level in rural areas,"
print "and you might be lucky and see", visible_urban, "in an urban area"

print
# Exercise 5
milky_stars = 10e11
galaxies = 10e11
print "There are about %d in our galaxy, the milky way," % milky_stars
print "and an estimated %d galaxies in the universe" % galaxies
print "This means somewhere arround", milky_stars * galaxies, "stars in the universe"
print "(Yes, I have known about %s for %d years, but I don't like\nthe %s inplementation)" % ("format strings", 20, "python")

# sidenote: while searching for the "answers" to "how many stars", google suggested the question
# "how many stars are there in our solar system"...
# *sigh*

print
# Exercise 6
