# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jesse Rodriguez
# Section:      102 M02
# Assignment:   Lab 3
# Date:         10 september 2026
# UIN:          239000380

from math import*
print ("Part 1")
h = float(input("Enter the height of the door: "))
w = float(input("Enter the width of the door: ")) 
r = w/sqrt(2)
arc_height = r - w/2 
rectangle_area = (h-arc_height) * w
arc_area = (pi*r**2)/4 - (r**2)/2
a = rectangle_area + arc_area
print (f"The area of the door is {a:.2f}")
# my math was so wrong the first time didn't even think to check it
print ("\nPart 2")
h1 = float(input("Enter the height of the pyramid: "))
s = sqrt(2) *h1
b_a = s**2
triangle_area = (sqrt(3)/4) * s**2
s_a =  b_a + 4 * triangle_area
print (f"The surface area of the pyramid is {s_a:.2f}")
print ("\nPart 3")
t_a = float(input("Enter the area of a triangle:"))
a = sqrt((4 * t_a) / sqrt(3))
print (f" The equilateral triangle has sides with length {a:.2f}")
b= sqrt(2*a**2 + 2*sqrt(a**4-4*t_a**2))
print (f"The isosceles triangle has two sides with lengths {a:.2f} and one side with length {b:.2f}")
c = (2*t_a)/b
d = sqrt(c**2 + b**2)
print (f"The right triangle has sides with lengths {b:.2f}, {c:.2f}, and {d:.2f}")
e = sqrt(a**2 + d**2 - sqrt(4*a**2*d**2 - 16*t_a**2))
print (f"The arbitrary triangle has sides with lengths {a:.2f}, {d:.2f}, and {e:.2f}")
# solving for b and e was torture