import random


board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
playerSign = 'x'
computerSign = 'o'

def board_clear():
    global board
    board = [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]

def checkOccupied(row,col):
    if board[row][col] != '-':
        return "It is already occupied."
def computerMove():
    global board
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                empty.append((i, j))
    if empty:
        i, j = random.choice(empty)
        board[i][j] = computerSign


def checkWinner():
    global board
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != "-":
        return board[2][0]
    for row in board:
        for cell in row:
            if cell == "-":
                return None
    return "tie"
