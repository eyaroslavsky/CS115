board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def printBoard(board):
    for row in range(3):
        for col in range(3):
            print(board[row][col], end='')
            if col != 2:
                print('|')
        if row != 2:
            print('\n')
            print('-----')
            print('\n')

def boardFull(board):
    full = True
    for row in range(3):
        for col in range(3):
            full = full and board[row][col] != ' '
    return full
