# Task 2
# Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

def calcArea(rad):
    return math.pi * rad * rad

# Taking the user input and calculate the area
rad = float(input("Enter the radius of the circle: "))
area = calcArea(rad)

# Printing the result with only 3 numbers after the decemal point
print(f"The area of the circle with radius {rad} is {area:.3f}")
