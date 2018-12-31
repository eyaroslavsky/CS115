from cs115 import *

L = ["cat", "mouse", "mole"]

def powerset(L):
    '''The set of sub-lists of L. The sub-lists
    should be in the same order as in L, but in the order
    of sub-lists is arbitrary.

    For example, powerset(["cat", "mouse", "mole"]) could
    return ([], ["cat"], ["mouse"], ["mole"], ["cat", "mouse"],
    ["cat", "mole"], ["mouse", "mole"], ["cat", "mouse", "mole"]]
    '''
    if L == []:
        return [[]]
    else:
        lose = powerset(L[1:])
        use = map(lambda M: [L[0]] + M, powerset(L[1:]))
        return lose + use 


def isSubset(L, M):
    '''Whether every element of L is in M'''
    if L == []:
        return True
    return L[0] in M and isSubset(L[1:],M)
    

def subset(target, L):
    '''Whether some elements of L add up to target, assuming
    target >= 0 and all elements of L are non-negative numbers'''
    if target == 0:
        return True
    elif L == []:
        return False
    elif L[0] > target:
        return subset(target, L[1:])
    else:
        lose = subset(target, L[1:])
        use = subset(target - L[0], L[1:])
        return use or lose


def knapsack(capacity, valueList):
    '''Max value of possible within capacityh, assuming capacity >=0,
    given list of items [weight, value]'''
    if valueList == [[]] or capacity == 0:
        return 0
    elif 
