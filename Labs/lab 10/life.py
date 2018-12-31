#
# life.py - Game of Life lab
#
# Name: Edward Yaroslavsky eyarosla 11/8/18
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

from cs115 import *
import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """returns a 2d array with "height" rows and "width" cols"""
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    """this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width,height):
    """creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells."""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width, height):
    """returns a 2d array of all live cells - with the value of 1
    - except for a one-cell-wide border of empty cells (with the value of 0)
    around the edge of the 2d array."""
    A = createBoard(width, height)
    for row in range(1,width-1):
        for col in range(1,height-1):
            A[row][col] = 1
    return A

def randomCells(width, height):
    """returns an array of randomly-assigned 1's and 0's
    except that the outer edge of the array is still completely empty"""
    A = createBoard(width, height)
    for row in range(1,width-1):
        for col in range(1,height-1):
            A[row][col] = random.choice([0,1])
    return A

def copy(A):
    """will make a deep copy of the 2d array A"""
    Arr = createBoard(len(A[0]),len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            Arr[row][col] = A[row][col]
    return Arr

def innerReverse(A):
    """that takes an old 2d array (or "generation") and then creates a new generation
    of the same shape and size. However, the new generation should be
    the "opposite" of A's cells everywhere except on the outer edge."""
    Arr = copy(A)
    for row in range(1,len(A[0])-1):
        for col in range(1,len(A)-1):
            if Arr[row][col] == 0:
                Arr[row][col] = 1
            else:
                Arr[row][col] = 0
    return Arr

def countNeighbors(row,col,A):
    """returns the number of live neighbors for a cell
    in the board A at a particular row and col."""
    count = 0
    if A[row-1][col-1] == 1:
        count+=1
    if A[row][col-1] == 1:
        count+=1
    if A[row-1][col] == 1:
        count+=1
    if A[row+1][col] == 1:
        count+=1
    if A[row][col+1] == 1:
        count+=1
    if A[row+1][col+1] == 1:
        count+=1
    if A[row-1][col+1] == 1:
        count+=1
    if A[row+1][col-1] == 1:
        count+=1
    return count

def next_life_generation(A):
    """makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0."""
    newA = copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            count = countNeighbors(row,col,A)
            if count < 2 or count > 3:
                newA[row][col] = 0
            if count == 3 and newA[row][col] == 0:
                newA[row][col] = 1
    return newA
