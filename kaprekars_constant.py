# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Yulian Villarreal
# Section: M02
# Assignment: Lab Topic 7 (individual)
# Date: 1/10/2026
user_number = input("Enter a four-digit integer: ") # Receive input
current_num = int(user_number) # Set it into a number
initial_string = f"{current_num:04d}" # convert to a string so it can be put into a list
sequence = [user_number] # set list to be able to put them in their orders
iterations = 0 # set iteration to find out how many times we get the desired number
while current_num != 6174 and current_num != 0:
    iterations += 1
    descending = "".join(sorted(initial_string, reverse=True))
    ascending = "".join(sorted(initial_string))
    ascending = int(ascending) # Set back into numbers to be able to do math
    descending = int(descending)
    current_num = descending - ascending
    initial_string = f"{current_num:04d}"
    sequence.append(str(current_num))
print(" > ".join(sequence))
print(f"{user_number} reaches {current_num} via Kaprekar's routine in {iterations} iterations")