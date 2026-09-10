# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Jose Godoy
# Jesse Rodriguez
# Yulian Villareal
# Amber Perez
# Section: M02
# Assignment: Lab 3 group
# Date: 09/09/2026
t1= float(input("Enter time 1: "))
x1= float(input("Enter the x position of the object at time 1: "))
y1= float(input("Enter the y position of the object at time 1: "))
z1= float(input("Enter the z position of the object at time 1: "))
t2= float(input("Enter time 2: "))
x2= float(input("Enter the x position of the object at time 2: "))
y2= float(input("Enter the y position of the object at time 2: "))
z2= float(input("Enter the z position of the object at time 2: "))
mx= (x2 - x1) / (t2 - t1)
my= (y2 - y1) / (t2 - t1)
mz= (z2 - z1) / (t2 - t1)
i= (t2-t1)/4
# y= m (x-x1) + y1
#y = f.123
#m = mx my mz
#x = i+ 1
# y1 = x1 y1 z1
fx1= mx*(i+ t1-(t1))+x1
fx2= mx*(2*i+ t1-(t1))+x1
fx3= mx*(3*i+ t1-(t1))+x1
fy1= my*(i+ t1-(t1))+y1
fy2= my*(2*i+ t1-(t1))+y1
fy3= my*(3*i+ t1-(t1))+y1
fz1= mz*(i+ t1-(t1))+z1
fz2= mz*(2*i+ t1-(t1))+z1
fz3= mz*(3*i+ t1-(t1))+z1
print(f"\nAt time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")
print(f"At time {t1+i:.2f} seconds the object is at ({fx1:.3f}, {fy1:.3f}, {fz1:.3f})")
print(f"At time {t1+2*i:.2f} seconds the object is at ({fx2:.3f}, {fy2:.3f}, {fz2:.3f})")
print(f"At time {t1+3*i:.2f} seconds the object is at ({fx3:.3f}, {fy3:.3f}, {fz3:.3f})")
print(f"At time {t2:.2f} seconds the object is at ({x2:.3f}, {y2:.3f}, {z2:.3f})")   
#this was a long but satisfying one