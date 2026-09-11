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
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
p1 = (0,x)
p2 = (x+y,0)
p3 = (x,y)
x1,y1 = p1
x2,y2 = p2
x3,y3 = p3 
a = sqrt((x2-x1)**2 + (y2-y1)**2)
b = sqrt((x3-x2)**2 + (y3-y2)**2)
c = sqrt((x1-x3)**2 + (y1-y3)**2)
s = (a+b+c)/2
heron_formula = sqrt(s*(s-a)*(s-b)*(s-c))
print (f"The area of the triangle is{heron_formula: .3f}" )