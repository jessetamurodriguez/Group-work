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
cost = float(input("How much did it cost? "))
change = amount_paid - cost

if change < 0:
    print("The amount paid is less than the cost of the item.")
else:
    print(f"You received ${change:.2f} in change. That is...")
    
    # Convert to total cents as an integer to avoid floating-point bugs
    cents = round(change * 100)
    
    # Calculate each coin type using integer division and modulo
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents // 1
    
    # Create a list to hold the text for each non-zero coin
    output_parts = []
    
    if quarters > 0:
        output_parts.append(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")
    if dimes > 0:
        output_parts.append(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")
    if nickels > 0:
        output_parts.append(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")
    if pennies > 0:
        output_parts.append(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")
        
    # Join them together into a clean sentence
    print("\n".join(output_parts))
