# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Yulian Villarreal
# Section: M02
# Assignment: Lab Topic 7 (individual)
# Date: 2/10/2026
# Get user input
list_of_numbers = input("Enter numbers: ").split()
# Convert string into integers
numbers = []
for item in list_of_numbers:
    numbers.append(int(item))
split_found = False
for i in range(1, len(numbers)):
    left_part = numbers[:i]
    right_part = numbers[i:]
    left_sum = 0
    for num in left_part:
        left_sum += num
    right_sum = 0
    for num in right_part:
        right_sum += num
    if left_sum == right_sum:
        print(f"Left: {left_part}")
        print(f"Right: {right_part}")
        print(f"Both sum to {left_sum}")
        split_found = True
        break
if not split_found:
    print("Cannot split evenly")