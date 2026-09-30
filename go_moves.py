# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yulian Villarreal
# Jese Rodriguez
# Amber Perez
# Jose Godoy
# Section: M02
# Assignment: Lab Topic 7 (team)
# Date: 29/9/2026
# set the color change
begin = "\x1b[1m"
end = "\x1b[39m\x1b[22m"
red = "\x1b[31m"
blue = "\x1b[34m"
green = "\x1b[32m"
# style stones using circle values
black_stone = begin + blue + chr(9679) + end # blue filled circle
white_stone = begin + red + chr(9675) + end # red empty circle
empty_point = "."
# Initialize the 9x9 board using for loops
board = []
for i in range (9):
    row = []
    for j in range(9):
        row.append(empty_point)
    board.append(row)

is_black_turn = True
print(begin + green + "=== Welcome to the 9x9 Go Board Simulation" + end)
# Main game loop
while True:
    print("\n  1 2 3 4 5 6 7 8 9")
    for r in range (9):
        print(f"{r + 1} ", end=" ")
        for c in range(9):
            print(board[r][c], end=" ")
        print()
    print() # print empty loop on outer loop to start new row
    # Know whos turn it is
    if is_black_turn:
        player_name = "Black (●)"
    else:
        player_name = "White (○)"
    # Get input from user
    user_input = input(player_name + "'s turn (Row Col or 'stop'): ").strip().lower()
    if user_input == "stop":
        print("Session closed safely.")
        break
    # Check if input has both parts (row col)
    parts = user_input.split()
    if len(parts) != 2:
        print(begin + red + "Error: Invalid entry. Provide two numbers (e.g., 3 5)." + end)
        continue
    # Check the input has numbers and not any other signs
    if not parts[0].isdigit() or not parts[1].isdigit():
        print(begin + red + "Error: Input must be numbers only!" + end)
        continue
    # Convert strings to integers
    row = int(parts[0]) - 1
    col = int(parts[1]) - 1
    # Do some boundary checks
    if row < 0 or row >= 9 or col < 0 or col >= 9:
        print(begin + red + "Error: Coordinates must be within 1 and 9!" + end)
        continue
    # Check for occupied spaces
    if board [row][col] != empty_point:
        print(begin + red + "Error: A stone already exists there! Try again." + end)
        continue
    # Set stone in inputted values and change turns
    if is_black_turn:
        board[row][col] = black_stone
        is_black_turn = False
    else:
        board[row][col] = white_stone
        is_black_turn = True