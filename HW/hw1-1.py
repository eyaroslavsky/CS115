'''Edward Yaroslavsky
I pledge my honor that I have abided by the Stevens Honor System'''

from cs115 import *

def add(x,y):
    '''Returns the sum of x and y'''
    return x + y

def mult(x,y):
    '''Returns the product of x and y'''
    return x * y

def factorial(n):
    '''Returns n! from positive input n'''
    return reduce(mult,range(1,n+1))

def mean(L):
    '''Returns the mean of list L'''
    return (reduce(add, L) / len(L))

def divides(n):
    '''Returns the function div'''
    def div(k):
        '''Returns a True or False depending on whether n is divisible by k'''
        return n % k == 0
    
    return div

def prime(n):
    '''Returns True or False depending on whether n is prime
    input n: a positive integer greater 1'''
    if (n == 0 or n == 1):
        return False
    booleanList = map(divides(n),range(2,n))       
    return sum(booleanList) == 0
