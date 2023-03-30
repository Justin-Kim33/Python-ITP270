#!/bin/python3

# Get the planet number as input

planet_number = int(input("Enter the planet number: "))



# Get the weight on earth as input

weight_on_earth = float(input("Enter the weight on earth (in kg): "))



# Define the relative gravity dictionary

relative_gravity = {

    1: 0.91,

    2: 0.38,

    3: 2.34,

    4: 1.06,

    5: 0.92,

    6: 1.19

}



# Calculate the weight on the destination planet

weight_on_destination_planet = weight_on_earth * relative_gravity[planet_number]



# Print the weight on the destination planet

print("Weight on the destination planet is: {:.2f} kg".format(weight_on_destination_planet))


