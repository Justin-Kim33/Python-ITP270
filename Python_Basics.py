#!/bin/python3

# Step 1: Creating variables for name, age, and degree program

name = ""

age = 0

degree_program = ""



# Step 2: Taking user input for all three variables

name = input("Enter your name: ")

age = int(input("Enter your age: "))

degree_program = input("Enter your degree program: ")



# Step 3: Calculating remaining age and storing it in a variable

remaining_age = (age * 3) % 2



# Step 4: Printing the message with string concatenation

print("Hello, my name is " + name + ". My remaining age is " + str(remaining_age) + " and I am studying " + degree_program + " degree program.")


