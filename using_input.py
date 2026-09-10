# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jesse Rodriguez
# Section:      102 M02
# Assignment:   Lab 3
# Date:         10 september 2026
# UIN:          239000380

#reynolds number (Re)
#Re= uL/v
from math import *
print ("This program calculates the Reynolds number given velocity, length, and viscosity")
V = float(input("Please enter the velocity (m/s): "))
L = float(input("Please enter the length (m): ")) 
u = float(input("Please enter the viscosity (m^2/s): "))
Re = (V*L)/u
print(f"Reynolds number is {Re:.0f}")
#Braggs law nλ=2dsintheta
print("\nThis program calculates the wavelength given distance and angle")
d = float(input("Please enter the distance (nm): "))
theta = float(input("Please enter the angle (degrees): "))
nλ= 2*d*sin(radians(theta))
print(f"Wavelength is {nλ:.4f} nm")
# arps equation q(t)=qi/(1+(bDi)t)^(-1/b)
print (f"\nThis program calculates the production rate given time, initial rate, and decline rate")
t = float(input("Please enter the time (days): "))
qi = float(input("Please enter the initial rate (barrels/day): "))
b = .8
Di = float(input("Please enter the decline rate (1/day): "))

q = qi/(1+(b*Di*t))**(1/b)
print(f"Production rate is {q:.2f} barrels/day")
print(f"\nThis program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
#Tsiolkovsky rocket equation Δv=ve*ln(m0/mf)
m0 = float(input("Please enter the initial mass (kg): "))
mf = float(input("Please enter the final mass (kg): "))
ve = float(input("Please enter the exhaust velocity (m/s): "))
Δv=ve*log (m0/mf)
print(f"Change of velocity is {Δv:.1f} m/s")