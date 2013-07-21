# number of cars
cars = 100
# number of spaces in the car
space_in_a_car = 4.0
# amount of drivers
drivers = 30
# amount of passengers
passengers = 90
# cars that don't have drivers assigned
cars_not_driven = cars - drivers
# cars that have drivers assigned == to amount of drivers
cars_driven = drivers
#capacity in all the cars
carpool_capacity = cars_driven * space_in_a_car
#average passengers per car
avarage_passengers_per_car = passengers / cars_driven

print "There are " , cars , " cars available."
print "There are only ", drivers, " drivers available."
print "There will be ", cars_not_driven, " empty cars today."
print "We can transport ", carpool_capacity, " people today."
print "We have ", passengers, " to carpool today."
print "We need to put about ", avarage_passengers_per_car, " in each car."
