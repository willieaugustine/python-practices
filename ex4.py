cars = 100
space_in_a_car =4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are",cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be",cars_not_driven, "empty cars today."
print "We can transport",carpool_capacity, "people today."
print "We have",passengers, "to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
metric_height = height * 2.54
metric_weight = weight * 0.453592
print "to the rest of the world, % is %2.2f cm tall." % (name, metric_height)
print "And they would say he is %2.4f kg heavy." % metric_weight
