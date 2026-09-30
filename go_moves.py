# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:Jesse Rodriguez Yulian Villareal Jose Godoy Amber Perez
# Section: M02
# Assignment: Lab 7 group
# Date: 09/30/2026

board = []
for i in range(9):
    row = []
    for j in range(9):
        row.append(".")
    board.append(row)
s = "O"
print("Black = O, White = o")
print("Rows go down; columns go right. Use numbers 1-9.")
print("Enter stop for the row to quit.")
while True:
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(board[r][c], end="")
        print()
    print(f"{s}'s turn")
    r = input("Enter row: ")
    if r == "stop":
        break
    r = int(r) - 1
    c = int(input("Enter column: ")) - 1
    if r < 0 or r > 8 or c < 0 or c > 8:
        print ("Use numbers on the board 1 - 9")
        