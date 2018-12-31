'''Edward Yaroslavsky eyarosla 11/17/18
I pledge my honor that I have abided by the Stevens Honor System.

HW 11'''

from cs115 import *
from random import randint

# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            # TODO print a message telling the user they won
            print("You win! Good job!")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            # TODO print a message telling the user the computer won
            print("Computer wins! Maybe you'll do better next time?")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles

    while True:
        num_piles = int(input("How many piles do you want to play with? "))
        if num_piles > 0:
            break
        print("Please print a valid number")
        
    piles = [0] * num_piles
    for x in range(len(piles)):
        while True:
            ans = int(input("How many in pile " + str(x) + "? "))
            if ans >= 0:
                break
            print("Please print a valid number")
        piles[x] = ans

        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    i = 0
    while i < len(piles):
        print("pile " + str(i) + " = " + str(piles[i]))
        i += 1


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    while True:
        pileNum = int(input("Which pile? "))
        if pileNum in range(0,num_piles) and piles[pileNum] > 0:
            return pileNum
        print("Please print a valid number")


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    
    while True:
        numRemove = int(input("How many? "))
        if numRemove in range(1,piles[pnum]+1):
            return numRemove
        print("Please print a valid number")


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles

    nimSum = piles[0]
    
    for x in piles[1:]:
        nimSum = nimSum ^ x

    return nimSum

def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 

    index = 0
    
    for x in piles:
        if not (x == 0):
            pileSum = x ^ game_nim_sum()
            if pileSum == 0:
                return (index,x)
            elif pileSum <= x:
                return (index,pileSum)
        index += 1

    while True:
        randomPile = randint(0,len(piles))
        if piles[randomPile] > 0:
            print("RANDOM")
            return (randomPile,1)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    bestPlay = opt_play()
    piles[bestPlay[0]] = piles[bestPlay[0]] - bestPlay[1]
    print("I remove " + str(bestPlay[1]) + " from pile " + str(bestPlay[0]))

    
#   start playing automatically
if __name__ == "__main__" : play_nim()
