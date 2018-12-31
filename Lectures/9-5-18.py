'''import cs115

def add(x,y):
    return x + y

def f(L):
    #assume L is a list of numbers; return its sum
    return cs115.reduce(add,L) '''


from cs115 import *
#from cs115 import reduce, range

def add(x,y):
    return x + y

def f(L):
    '''assume L is a list of numbers; return its sum'''
    return reduce(add,L)


def multiply(x,y):
    return x*y

def fact(N):
    return reduce(multiply,range(1,N+1))


def span(L):
    '''assuming L is a list of numbers, return diff of max and min of L'''
    m = reduce(min,L)
    n = reduce(max,L)
    return n - m


def gauss(N):
    return reduce(add,range(1,N+1))


def square(N):
    return N*N

def sumOfSquares(N):
    return reduce(add,map(square,range(1,N+1)))



