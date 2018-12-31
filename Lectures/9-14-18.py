from cs115 import *

def prime(n):
    '''Returns True or False to check if n is prime'''
    possibleDivisors = range(2,n)
    divisors = filter(lambda X: n % X == 0, possibleDivisors)
    return len(divisors) == 0

def sieve(L):
    '''Eratosthenes; assume L is a list of naturals'''
    if L == []:
        return []
    return [L[0]] + sieve(filter(lambda x: x % L[0] != 0, L[1:]))

def primes(n):
    '''The primes up to n'''
    return sieve(range(2,n+1))
