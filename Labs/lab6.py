'''
Created on 10/11/18
@author: Edward Yaroslavsky eyarosla
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1

#42 in base 2 is 101010
#The least significant bit in an odd number will be 1 and 0 in an even.
#The value of the original number is being divided by 2 and then rounded down.
#For an even number, we would shift over the value by 1 place and add a 0 to the end.
#For an odd number, we would shift over the value by 1 place and add a 1 to the end.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif isOdd(n):
        return numToBinary(n//2) + "1"
    else:
        return numToBinary(n//2) + "0"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def binaryToNumHelper(s,place):
        if s == "":
            return 0
        elif s[-1] == "1":
            return binaryToNumHelper(s[:-1],place+1) + 2**(place)
        else:
            return binaryToNumHelper(s[:-1],place+1)
    return binaryToNumHelper(s,0)

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    num = numToBinary(binaryToNum(s)+1)
    if len(num) > 8:
        return num[1:]
    if len(num) < 8:
        return (8-len(num))*"0" + num
    return num

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n > 0:
        return count(increment(s), n-1)

#2012 is the ternary representation of 59 since 2 ones + 1 three + 0 nines + 2 twenty-sevens
#makes up 59.

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    else:
        return numToTernary(n//3) + str(n%3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    def ternaryToNumHelper(s,place):
        if s == "":
            return 0
        elif s[-1] == "1":
            return ternaryToNumHelper(s[:-1],place+1) + 3**place
        elif s[-1] == "2":
            return ternaryToNumHelper(s[:-1],place+1) + 2*(3**place)
        else:
            return ternaryToNumHelper(s[:-1],place+1)
    return ternaryToNumHelper(s,0)
