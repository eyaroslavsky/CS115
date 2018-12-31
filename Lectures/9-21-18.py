from cs115 import *

def allCoins(coins):
    '''Returns penny nickel dime from [[1,'penny'],[5,'nickel'],[10,'dime']]''' 
    return reduce(lambda str1, str2: str1 + ' ' + str2,
                  map(lambda pairs: pairs[1], coins))

def exp(n,k):
    '''n**k, assuming k >= 0 and n is a number'''
    if k==0:
        return 1
    return n * exp(n, k-1)

def expfast(n,k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        t = expfast(n, k//2)
        return t*t
    else:
        return n * expfast(n, k-1)

def exptail(n,k):
    '''n**k, computed by tail recursion'''
    def ext(accumulator, n, k):
        if k == 0:
            return accumulator
        else:
            return ext(n * accumulator, n, k-1)
    return ext(1, n, k)

def reverse(L):
    if L == []:
        return []
    else:
        return reverse(L[1:]) + [L[0]]

def reverse2(L):
    def rev(acc, L):
        if L == []:
            return acc
        else:
            return rev(L[0] + acc, L[1:])
    return rev([],[a,b,c])
