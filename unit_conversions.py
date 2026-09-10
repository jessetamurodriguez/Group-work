# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Amber Perez
# Jose Godoy
# Jesse Rodriguez
# Yulian Villarreal
# Section: MO2
# Assignment: Lab 3
# Date: 09/09/26

from math import* #yogurt

x: float = float(input("Please enter the quantity to be converted: "))
newtons = (x * 4.44822)
print(f"{x:.2f} pounds force is equivalent to {newtons :.2f}", "newtons")


feet = (x * 3.28084)
print(f"{x:.2f} meters is equivalent to {feet:.2f}", "feet")


pascals = (x * 101.325)
print(f"{x:.2f} atmospheres is equivalent to {pascals :.2f}", "kilopascals")


watts = (x * 3.41214)
print(f"{x:.2f} watts is equivalent to {watts :.2f}", "BTU per hour")


gallons = (x * 15.85033)
print(f"{x:.2f} liters per second is equivalent to {gallons :.2f}", "US gallons per minute")


fahrenheit = (x * 9/5 + 32)
print(f"{x:.2f} degrees Celsius is equivalent to {fahrenheit :.2f}", "degrees Fahrenheit")