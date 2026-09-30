# By submitting this assignment, I agree to the following:
# Aggies do not lie, cheat, or steal, or tolerate those who do.
# I have not given or received any unauthorized aid on this assignment.
# Name
# Jose Godoy
# Section: M02
# Assignment: Lab 7 (individual_)
# Date:9/28/2026
x= input("What is your name? ")
# x is og name
vca=(x[0]=="A" or x[0]=="E" or x[0]=="I" or x[0]=="O" or x[0]=="U" or x[0]=="Y")
vcb=(x[1]=="a" or x[1]=="e" or x[1]=="i" or x[1]=="o" or x[1]=="u" or x[1]=="y")
#checks for the first 2 vowels
i=1
while vcb==0:
    i+=1
    vcb=(x[i]=="a" or x[i]=="e" or x[i]=="i" or x[i]=="o" or x[i]=="u" or x[i]=="y")
    #finds where the vowel is
y=x[i:]
#keeps name from first vowel onward
if vca == 1:
    p=x[0].lower()
    y=f"{p}{x[1:]}"
#if it starts with a vowel the first is lowecase
# y is the start of the name starting at vowel
print(f"{x}, {x}, Bo-B{y}")
print(f"Banana-Fana Fo-F{y}")
print(f"Me Mi Mo-M{y}")
print(f"{x}!")