# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Jose Godoy
# Jesse Rodriguez
# Yulian Villareal
# Amber Perez
# Section: M02
# Assignment: Lab 6 group
# Date: 09/23/2026
import math
x= float(input("Enter a value for x: "))
while x <=0 or x >2:
    x=(float(input("Out of range! Try again: ")))
t= float(input("Enter the tolerance: "))
ex=1
ant=t+1
#gurantees a turn
#.3 and .00003
while not ant<t:
    if ex==1:
        nt=(x-1)
        nts=nt
        #first cycle only
    elif ex%2 ==0:
        it=((x-1)**ex)/ex
        nts=nts-it
        nt=((x-1)**ex)/ex
        # all even terms are subtracted
    elif ex%2 ==1:
        it=((x-1)**ex/ex)
        nts+=it
        nt=((x-1)**ex)/ex
        # all odd terms are added
    ex+=1
    ant=abs(nt)
    #checks the absolute value of the next term
if ex%2==0:
    nts=nts-nt
elif ex%2==1:
    nts=nts+nt
print(f"ln({x}) is approximately", nts)
ln=math.log(x)
print(f"ln({x}) is exactly", ln)
dif=abs(ln-nts)
print("The difference is", dif)