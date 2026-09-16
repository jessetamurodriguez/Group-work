# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Amber Perez
# Jose Godoy
# Jesse Rodriguez
# Yulian Villarreal
# Section: MO2
# Assignment: Lab 4 team
# Date: 09/16/26
amount_paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost?: "))
change = amount_paid - cost
if change < 0:
    print("The amount paid is less than the cost of the item. Please provide sufficient funds.")
else:
    print(f"You recieved ${change:.2f} in change. That is...")

if change >= 0.25:
    print (str(int(change // 0.25))+ " quarters")
    change = change - (int(change // 0.25) * 0.25)
if change >= 0.10:
    print (str(int((change % 0.25) // 0.10))+ " dimes")
    change = change - (int((change % 0.25) // 0.10) * 0.10)
if change >= 0.05:
    print (str(int(((change % 0.25) % 0.10) // 0.05))+ " nickels")
    change = change - (int(((change % 0.25) % 0.10) // 0.05) * 0.05)
if change >= 0.01:
    print (str(int((((change % 0.25) % 0.10) % 0.05)// 0.01))+ " pennies")