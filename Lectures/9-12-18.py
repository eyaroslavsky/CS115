from cs115 import *

def divides(n):
    def div(k):
        return n % k == 0
    return div

def divisibles(n,L):
    '''assume L is a list of integers; return a list of the ones divisible by n'''
    if L == []:
        return []
    elif divides(L[0])(n):
        return [L[0]] + divisibles(n,L[1:])
    else:
        return divisibles(n,L[1:])

def testDivisibles():
    print(divisibles(3,[1,6,4,9]) == [6,9])


words = ['']

def makeLen(n):
    '''Assume n is a non-negative integer. Return a function.
    That function applies to strings.
    It concatenates * characters to the given string to make its length at least n.'''
    def padIt(word):
        length = len(word)
        return word + ((n-length) * "*")
    return padIt

def pad(words):
    '''Assume words is a non-empty list of strings. Let n be the length of the longest.
    Return a list of the samea strings excpet with enough * charcaters appended to make
    each one length n.'''
    maxLength = max(map(len,words))
    return map(makeLen(m),words)
