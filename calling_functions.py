# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jesse Rodriguez
# Section:      102 M02
# Assignment:   Lab 3
# Date:         10 september 2026
# UIN:          239000380

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# Your code goes here
s = float(input("Please enter the side length: "))
t_a = (sqrt(3)/4) * s**2
printresult("triangle", s, t_a)
s_a = s**2
printresult("square", s, s_a)
pent_a = (1/4) * sqrt(5 * (5 + 2 * sqrt(5))) * s**2
printresult("pentagon", s, pent_a)
hex_a = (3 * sqrt(3) / 2) * s**2
printresult("hexagon", s, hex_a)
dodec_a = (3 * (sqrt(3) + 2)) * s**2
printresult("dodecagon", s, dodec_a)