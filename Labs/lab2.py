'''Edward Yaroslavsky 9/13/18
I pledge my honor that I have abided by the Stevens Honor System'''

from cs115 import *

def dot(L, K):
    '''Returns the dot product of lists L and K.'''
    if L == []:
        return 0
    elif K == []:
        return 0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])

def explode(S):
    '''Returns a list of the letters in String S.'''
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])

def ind(e, L):
    '''Returns the index at which element e is found at in sequence L.'''
    if L == [] or L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e,L[1:])

def removeAll(e, L):
    '''Returns a new list that removes all the elements e from list L on the top-level.'''
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])


def even(X):
    '''Returns True if X is even and false otherwise.'''
    if X % 2 == 0:
        return True
    return False

def myFilter(f, L):
    '''Returns a new list after testing function f on list L.
    If f returns True on an element of L then this element will be part of the new list.'''
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])


def myLen(L):
    '''len(L), assuming L is a list of numbers'''
    if L == []:
        return 0
    else:
        return 1 + myLen(L[1:])

def deepReverse(L):
    '''Returns the reversal of list L. Applies to the deeper level of lists as well.'''
    if L == []:
        return []
    elif isinstance(L[myLen(L)-1],list):
        return [deepReverse(L[myLen(L)-1])] + deepReverse(L[:myLen(L)-1])
    else:
        return [L[myLen(L)-1]] + deepReverse(L[:myLen(L)-1])
    
    
