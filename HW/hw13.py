'''Edward Yaroslavsky eyarosla 12/4/18
I pledge my honor that I have abided by the Stevens Honor System.

HW 13'''

class Board(object):
    '''A two-dimensional list/array of characters'''

    def __init__(self, width=7, height=6):
        '''Constructor for Board'''
        self.width = width
        self.height = height
        self.board = []
        for x in range(height):
            self.board += [[' '] * width]

    def __str__(self):
        '''String method for printing the Board'''
        display = ''
        for row in range(self.height):
            for col in range(self.width):
                display += '|' + self.board[row][col]
            display += '|\n'

        display += '--' * self.width + '\n'

        for x in range(self.width):
            display += ' ' + str(x)

        return display
        
    def allowsMove(self, col):
        '''Checks to see if a move is acceptable'''
        if ' ' not in self.board[0]:
            return False
        if col in range(0,self.width):
            for x in range(self.height):
                if self.board[x][col] == ' ':
                    return True
            return False
        else:
            return False

    def addMove(self, col, ox):
        '''Adds the move for the user currently playing'''
        if self.board[self.height-1][col] == ' ':
            if ox == 'X':
                self.board[self.height-1][col] = 'X'
            else:
                self.board[self.height-1][col] = 'O'
        else:
            for x in range(self.height):
                if self.board[x][col] != ' ':
                    if ox == 'X':
                        self.board[x-1][col] = 'X'
                        break
                    else:
                        self.board[x-1][col] = 'O'
                        break

    def setBoard( self, moveString ):
        """takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers"""
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def delMove(self, col):
        '''Deletes the most recent move from a specific column'''
        for x in range(self.height):
            if self.board[x][col] != ' ':
                self.board[x][col] = ' '
                break
        
    def winsFor(self, ox):
        '''Checks to see if a player has won'''
        horizontal = 0
        vertical = 0
        diag1 = 0
        diag2 = 0
        
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == ox:
                    horizontal += 1
                    if horizontal == 4 :
                        return True
                else:
                    horizontal = 0
            horizontal = 0

        for col in range(self.width):
            for row in range(self.height):
                if self.board[row][col] == ox:
                    vertical += 1
                    if vertical == 4:
                        return True
                else:
                    vertical = 0
            vertical = 0

        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.board[row][col] == ox:
                    diag1 += 1
                if self.board[row+1][col+1] == ox:
                    diag1 += 1
                if self.board[row+2][col+2] == ox:
                    diag1 += 1
                if self.board[row+3][col+3] == ox:
                    diag1 += 1
                if diag1 == 4:
                    return True
                diag1 = 0

        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.board[row][self.width-col-1] == ox:
                    diag2 += 1
                if self.board[row+1][self.width-col-2] == ox:
                    diag2 += 1
                if self.board[row+2][self.width-col-3] == ox:
                    diag2 += 1
                if self.board[row+3][self.width-col-4] == ox:
                    diag2 += 1
                if diag2 == 4:
                    return True
                diag2 = 0

        return False

    def hostGame(self):
        '''Starts and plays the game'''
        print('Welcome to Connect Four!')
        user = 1
        print(self)
        while True:
            
            while True:
                if user == 1:
                    choice = int(input("X's choice: "))
                    if self.allowsMove(choice):
                        self.addMove(choice, 'X')
                        user = 2
                        break
                    else:
                        print('Please pick an appropriate choice')
                        
            if ' ' not in self.board[0]:
                print('Tie')
                break
            
            print(self)

            if self.winsFor('X'):
                print('X wins -- Congratulations!')
                print(self)
                break

            while True:
                if user == 2:
                    choice = int(input("O's choice: "))
                    if self.allowsMove(choice):
                        self.addMove(choice, 'O')
                        user = 1
                        break
                    else:
                        print('Please pick an appropriate choice')

            if self.winsFor('O'):
                print('O wins -- Congratulations!')
                print(self)
                break

            if ' ' not in self.board[0]:
                print('Tie')
                break

            print(self)
        
                    



                    
