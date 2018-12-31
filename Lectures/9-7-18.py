from cs115 import *

def increment(k):
    '''Returns a function that adds k to a number'''
    def f(n):
        return n + k
    return f

'''
#For incPos(nums, n)
def increment(k):
    Returns a function that adds k to a number
    def f(n):
        if n > 0: return n + k
        else: return n
    return f
'''

def incAll(nums,n):
    '''Add n to every number in a given list of numbers'''
    return map(increment(n),nums)

def incPos(nums,n):
    '''Add n to every positive number, leaving the rest alone'''
    return map(increment(n),nums)
    
