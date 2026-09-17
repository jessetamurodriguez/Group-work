# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Jose Godoy
# Jesse Rodriguez
# Yulian Villareal
# Amber Perez
# Section: M02
# Assignment: Lab 4 group
# Date: 09/16/2026
############ Part A ############ 
a=(input("Enter True or False for a: "))
b=(input("Enter True or False for b: "))
c=(input("Enter True or False for c: "))
############ Part B ############
d=((a=="True")or(a=="t")or(a=="T"))
e=((b=="True")or(b=="t")or(b=="T"))
f=((c=="True")or(c=="t")or(c=="T"))
g=((d==True)and(e==True)and(f==True))
h=((d==True)or(e==True)or(f==True))
print( "a and b and c:", g)
print( "a or b or c:",h)
############ Part C ############
i=((not(d==False))and(e==False)or(not(e==False))and(d==False))
print("XOR:",i)
n=(int(d)+int(e)+int(f))
odd=(n==1 or n==3)
print ("Odd number:",odd)
