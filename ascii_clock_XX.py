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
# first we get a time 
tm = input("Enter the time (HH:MM): ")
ct= input ("Choose the clock type (12 or 24): ")
pc= input("Choose your preferred character: ")
# we translate 24 hr time to 12 hr time if asked in ct
if ct== "12":
    if int(tm[0:2])>12:
        tm = str(int(tm[0:2])-12)+tm[2:5]
# we identify what numbers are in the time
numbers = tm.split(":")
print(len(numbers))
if len(numbers) == 2:
    numbers.insert(0,"0")
print(numbers)
# we create the display board
board = []
for i in range(5):
    row = []
    for j in range(23):
        row.append(".")
    board.append(row)
#makes an initial board state
for  i in range(1):
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(board[r][c], end="")
        print()