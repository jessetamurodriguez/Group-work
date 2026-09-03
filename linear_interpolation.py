# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yulian Villarreal
#         Jesse Rodriguez
#         Amber Perez
#         Jose Godoy
# Section: M02
# Assignment: Lab Topic 2 (team)
# Date: 2/9/2026
#Calculate distance from Houston between minutes 10 and 55
from math import * 
x1= (10)
x2= (55)
y1= (2030)
y2= (23030)
x= (25)
slope= ((y2-y1)/(x2-x1))
y= float(slope * (x - x1)+ y1)
print("Part 1:")
print("For t =", x, "minutes, the position p =", y, "kilometers")
x = (300)
r = (6745)
c = (2 * pi * r)
y = float(slope * (x - x1) + y1) 
y %= c
print("Part 2:")
print("For t =", x, "minutes, the position p =", y, "kilometers") 
