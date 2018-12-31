'''Edward Yaroslavsky 9/14/18
CS115 - Hw 2
I pledge my honor that I have abided by the Stevens Honor System.'''


import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

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


def remove(letter, Rack):
    '''Removes a letter from a the list of letters, Rack'''
    if Rack == []:
        return []
    elif letter == Rack[0]:
        return Rack[1:]
    else:
        return [Rack[0]] + remove(letter, Rack[1:])

def isPossible(word, Rack):
    '''Returns a boolean to check if it is possible to
    create a certain word from the given list of letters, Rack'''
    if word == "":
        return True
    elif word[0] in Rack:
        return isPossible(word[1:], remove(word[0],Rack))
    return False

def listOfWords(Dict, Rack):
    '''Returns a list of all the words in the Dictionary that can be
    created out of the list of letters, Rack'''
    return filter(lambda word: isPossible(word, Rack),Dict)

def scoreList(Rack):
    '''Returns the list of a word alongside its wordScore of every word in
    the Dictionary, all put into a list'''
    return map(lambda word: [word,wordScore(word, scrabbleScores)],listOfWords(Dictionary, Rack))


def bestWord(Rack):
    '''Returns the list of a word alongside its wordScore of
    the highest wordScore available'''
    scorelist = scoreList(Rack)
    if scorelist == []:
        return ['',0]
    return reduce(lambda x,y: x if x[1] > y[1] else y, scorelist)
