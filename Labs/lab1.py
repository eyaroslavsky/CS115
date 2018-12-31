'''Edward Yaroslavsky
I pledge my honor that I have abided by the Stevens Honor System.'''

from cs115 import *
import math

def inverse(n):
    '''Returns the inverse of a number n'''        
    return 1/n

def add(x,y):
    '''Adds two numbers x and y together'''
    return x + y

def e(n):
    '''
    Takes positive input n and uses Taylor Expansion to
    sum up 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
    '''
    return reduce(add, map(inverse, map(math.factorial,range(n+1))))

def error(n):
    '''
    Finds the absolute value error in the
    e approximation of n Taylor polynomials
    '''  
    return abs(e(n) - math.e)
