from cs115 import *

def factorial(n):
    ans = 1
    for x in range(1,n+1):
        ans = ans * x
    return ans

def mapSqr(L):
    arr = []
    for x in L:
        arr += [L[x]*L[x]]
    return arr
