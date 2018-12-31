'''
Created on 9/24/18
@author:   Edward Yaroslavsky eyarosla
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
from cs115 import map

def giveChange(amount, coins):
    '''Returns the minimum number of coins from the currency list, coins,
    it takes for the value, amount, to be made up as first position in a list.
    The second position in the list is a list of all the coins used.'''
    if amount == 0:
        return [0,[]]
    elif coins == []:
        return [float("inf"),[]]
    elif amount < coins[-1]:
        return giveChange(amount, coins[:-1])
    else:
        use = giveChange(amount - coins[-1], coins)
        lose = giveChange(amount, coins[:-1])
        if use[0] < lose[0]:
            return [use[0]+1,[coins[-1]] + use[1]]
        else:
            return [lose[0],lose[1]]

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    return map(lambda word: [word,wordScore(word, scores)], dct)

def letterScore(letter, scoreList):
    '''Returns the scrabble score of an input letter based on the inputed score list.'''
    if scoreList == []:
        return 0
    elif scoreList[0][0] == letter:
        return scoreList[0][1]
    else:
        return letterScore(letter, scoreList[1:])

def wordScore(S, scoreList):
    '''Returns the sum of the scrabble score of all the letters in the input string.'''
    if S == "":
        return 0 
    else:
        return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n > len(L):
        return L
    elif n == 0:
        return []
    elif n < 0:
        return take(n+len(L), L)
    return [L[0]] + take(n-1, L[1:])


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n > len(L):
        return []
    elif n == 0:
        return L
    elif n < 0:
        return drop(n+len(L),L)
    return drop(n-1, L[1:])


