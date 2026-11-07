# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Yulian Villarreal
# Section:      102 M02
# Assignment:   Lab 11 (individual)
# Date:         6/11/2026
import csv
MONTHS_IN_YEAR = 12
def monthly_payment(principal, months, annual_rate): # Calculate the fixed monthly payment for the loan
    """Return the fixed monthly payment for the loan."""
    monthly_rate = annual_rate / MONTHS_IN_YEAR
    payment = principal * monthly_rate / (1 - (1 / (1 + monthly_rate)) ** months)
    return payment
# Format a number as dollars and cents, never as a negative zero
def money(value): # Format a number as dollars and cents, never as a negative zero
    """Format a number as dollars and cents, never as a negative zero."""
    if value < 0:
        value = 0.0
    return "$" + format(value, ".2f")
def main(): # Main function to run the loan calculator
    filename = input("Enter the output filename: ") # The name of the file to write the loan schedule to
    principal = float(input("Enter the principal amount: ")) # The initial loan amount
    months = int(input("Enter the term length (months): ")) # The total number of months for the loan
    annual_rate = float(input("Enter the annual interest rate: ")) # The annual interest rate
    payment = monthly_payment(principal, months, annual_rate) # The fixed monthly payment
    balance = principal
    total_interest = 0.0 # Total interest accrued over the life of the loan
    month = 0
    with open(filename, "w", newline="") as outfile: # Open the output file
        writer = csv.writer(outfile) # Create a CSV writer
        writer.writerow(["Month", "Total Accrued Interest", "Loan Balance"]) # Write the header row
        writer.writerow([month, money(total_interest), money(balance)]) # Write the initial row
        while balance >= 0.01: # Continue until the balance is fully paid off
            month = month + 1 # Increment the month
            monthly_interest = balance * annual_rate / MONTHS_IN_YEAR # Calculate the monthly interest
            total_interest = total_interest + monthly_interest
            balance = balance + monthly_interest - payment
            writer.writerow([month, money(total_interest), money(balance)])
main()