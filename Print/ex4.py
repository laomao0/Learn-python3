# number of cars
cars = 100
# number of space in a car
space_in_a_car = 4.0
# number of total drivers
drivers = 30
# number of total passengers
passengers = 90
# number of cars that are empty(without drivers)
cars_not_driven = cars - drivers
# number of cars that are driven
cars_driven = drivers
# number of total capabilities
carpool_capacity = cars_driven * space_in_a_car
# average number of passengers in each car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# int/int 类型的除法，最终的结果依旧是 float类型
