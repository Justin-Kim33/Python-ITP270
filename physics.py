#!/bin/python3

def f_to_c(f_temp):

    c_temp = (f_temp - 32) * 5/9

    return c_temp

f100_in_celsius = f_to_c(100)

print(f100_in_celsius) # Output: 37.77777777777778

def c_to_f(c_temp):

    f_temp = c_temp * (9/5) + 32

    return f_temp

c0_in_fahrenheit = c_to_f(0)

print(c0_in_fahrenheit) # Output: 32.0

def get_force(mass, acceleration):

    force = mass * acceleration

    return force

train_force = get_force(train_mass, train_acceleration)

print(train_force) # Output: 22680

print(f"The GE train supplies {train_force} Newtons of force.")

# Output: The GE train supplies 22680 Newtons of force.

def get_energy(mass, c=3*10**8):

    energy = mass * c ** 2

    return energy

bomb_energy = get_energy(bomb_mass)

print(bomb_energy) # Output: 9000000000000000

print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# Output: A 1kg bomb supplies 9000000000000000 Joules.

def get_work(mass, acceleration, distance):

    force = get_force(mass, acceleration)

    work = force * distance

    return work

train_work = get_work(train_mass, train_acceleration, train_distance)

print(train_work) # Output: 2268000

print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")

# Output: The GE train does 2268000 Joules of work over 100 meters.

done
