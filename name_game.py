# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Yulian Villarreal
# Section: M02
# Assignment: Lab Topic 7 (individual)
# Date: 1/10/2026
# Get name or input from user
user_name = input("What is your name? ")
vowels = [ 'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'] # Make a list of the vowels to check the start letters of names
i = 0
while i < len(user_name) and user_name[i] not in vowels:
    i += 1
if i == 0: # Check if first letter is a vowel
    y = user_name.lower()
else:
    y = user_name[i:].lower()

# Print the results
print(f"{user_name}, {user_name}, Bo-B{y}")
print(f"Banana-Fana Fo-F{y}")
print(f"Me Mi Mo-M{y}")
print(f"{user_name}!")