import random

def main():
    board =[[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

    board = randomize(board)
    moves = 0
    while is_solved(board) == False:
        show(board)
        row, col = solicit_row_and_col()
        touch(board, row, col)
        moves += 1
    show(board)
    print(f"You won with {moves} moves!")

def is_solved(board):
    counter = 0

    for i in range(5):
        counter += sum(board[i])
    
    if counter == 0:
        return True
    else:
        return False

def solicit_row_and_col():
    row = int(input("Please choose a row number (0-4): "))
    col = int(input("Please choose a column number (0-4): "))
    return row, col

def touch(board, row, col):
    if row > 0:
        board[row - 1][col] = abs(board[row - 1][col] - 1)
    if col > 0:
        board[row][col - 1] = abs(board[row][col - 1] - 1)
    if col < 4:
        board[row][col + 1] = abs(board[row][col + 1] - 1)
    if row < 4:
        board[row + 1][col] = abs(board[row + 1][col] - 1)
    board[row][col] = abs(board[row][col] - 1)

    return board    

def randomize(board):
    for i in range(69):
        touch(board, random.randint(0,4), random.randint(0,4))
    return board

def show(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                print("\N{BLACK SQUARE}  ", end = ' ')
            else:
                print("\N{WHITE SQUARE}  ", end = ' ')
            if j == 4:
                print("\n")


main()
