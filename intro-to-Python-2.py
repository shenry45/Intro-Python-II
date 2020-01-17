""" Intro to Python II - Guided Project
    This document contains examples for CS Intro to Python, module 2. Examples
    will highlight unique syntax rules in Python. Students will continue to
    practice creating elements such as lists, dictionaries, and functions. 
    Additionally, we will look at the CS problem-solving framework and practice
    using it to break down more complex problems.
"""
# RECAP: How do we...
# create a list of floating point temperatures?
# TODO

# in a single line, create a new list containing all of the temperatures from
# the above list that are greater than 90.0?
# TODO

# create a dictionary students in which their `id` is the key and their name
# is the `value`?
students = {}
students["name"] = "Tulip"
students["species"] = "Juniper"
students["brand"] = "Flower"

print(students)

# add a new student to our dictionary? modify an existing student entry?
# TODO

# When we write functions in different languages, it is important to know if
# arguments are passed by REFERENCE or VALUE.


def mult2(x): # x is a single integer value to be doubled
    # TODO
    pass


def mult2_list(x): # x is a list of integer values to be doubled
    # TODO
    pass

# UPER - Given a number of people, number of pizzas, and number of slices per
# pizza, write a function to evenly divide the slices between each person.
# 1. Understand
# 2. Plan
# 3. Execute
# TODO

# 4. Reflect
# UPER - Prompt a user to enter three, uique numbers as input, print out 
# which number is the largest of the three. 
# 1. Understand
# 2. Plan
# 3. Execute


def calc_largest():
    # TODO
    pass

# 4. Reflect
# UPER - Write a function that returns the "centered" average of an array of 
# ints, which we'll say is the mean average of the values, except ignoring the 
# largest and smallest values in the array. 
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3
# 1. Understand
# 2. Plan
# 3. Execute


def centered_average(nums):
    # TODO
    pass

# 4. Reflect