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
#makes an initial board state
s = "Black"
print("Black = ○, White = ●")
print("Rows go down; columns go right. Use numbers 1-9.")
print("Enter stop for the row to quit.")
# instructions to play
while True:
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(board[r][c], end="")
        print()
    while s=="Black":  # for black turn
        print(f"{s}'s turn")
        r = input("Enter row: ")
        if r == "stop":
            break
        r = int(r) - 1
        c = int(input("Enter column: ")) - 1
        if r < 0 or r > 8 or c < 0 or c > 8:
            print ("\x1b[1m" +"\x1b[31m" + "Use numbers on the board 1 - 9" + "\x1b[39m\x1b[22m")
            #display red text and stay on board
            break
        if not board[r][c]==".":
            print ("\x1b[1m" +"\x1b[31m" + "space is occupied try again" + "\x1b[39m\x1b[22m")
            # display red text and say space is occupied
            break
        board[r][c]=chr(9675)
        # empty dot
        s="White"
        for r in range(len(board)):
                for c in range(len(board[r])):
                    print(board[r][c], end="")
                print()
            #show board state after black
    while s=="White": # for white turn
        print(f"{s}'s turn")
        r = input("Enter row: ")
        if r == "stop":
            break
        r = int(r) - 1
        #translate move to list value
        c = int(input("Enter column: ")) - 1
        if r < 0 or r > 8 or c < 0 or c > 8:
            print ("\x1b[1m" +"\x1b[31m" + "Use numbers on the board 1 - 9" + "\x1b[39m\x1b[22m")
            break
        if not board[r][c]==".":
            print ("\x1b[1m" +"\x1b[31m" + "space is occupied try again" + "\x1b[39m\x1b[22m")
            break
        board[r][c]=chr(9679)
        # a full circle
        s="Black"
        # cycles back to the top
    if r=="stop":
        break
        #stops the game
