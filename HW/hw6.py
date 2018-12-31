'''
Created on 10/16/18
@author: Edward Yaroslavsky eyarosla
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1

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
        '''Keeps track of the position of the value's place.'''
        if s == "":
            return 0
        elif s[-1] == "1":
            return binaryToNumHelper(s[:-1],place+1) + 2**(place)
        else:
            return binaryToNumHelper(s[:-1],place+1)
    return binaryToNumHelper(s,0)

def compress(S):
    '''Takes a binary string S of length 64 as input and
    returns another binary string as output. The output binary string should be
    a run-length encoding of the input string.'''
    def compress_helperZero(S, consecutiveZero):
        '''Outputs the COMPRESSED_BLOCK_SIZE for the 0 component.'''
        if S == "" and consecutiveZero > 0:
            frontZero = (COMPRESSED_BLOCK_SIZE - len(str(numToBinary(consecutiveZero)))) * "0"
            return frontZero + str(numToBinary(consecutiveZero))
        elif S == "":
            return ""
        elif S[0] == "0":
            if consecutiveZero == binaryToNum(COMPRESSED_BLOCK_SIZE*"1"):
                return "1" * COMPRESSED_BLOCK_SIZE + compress_helperOne(S, 0)
            return compress_helperZero(S[1:], consecutiveZero+1)
        else:
            frontZero = (COMPRESSED_BLOCK_SIZE - len(str(numToBinary(consecutiveZero)))) * "0"
            return frontZero + str(numToBinary(consecutiveZero)) + compress_helperOne(S, 0)

    def compress_helperOne(S, consecutiveOne):
        '''Outputs the COMPRESSED_BLOCK_SIZE for the 1 component.'''
        if S == "" and consecutiveOne > 0:
            frontOne = (COMPRESSED_BLOCK_SIZE - len(str(numToBinary(consecutiveOne)))) * "0"
            return frontOne + str(numToBinary(consecutiveOne))
        elif S == "":
            return ""
        elif S[0] == "1":
            if consecutiveOne == binaryToNum(COMPRESSED_BLOCK_SIZE*"1"):
                return "1" * COMPRESSED_BLOCK_SIZE + compress_helperZero(S, 0)
            return compress_helperOne(S[1:], consecutiveOne+1)
        else:
            frontOne = (COMPRESSED_BLOCK_SIZE - len(str(numToBinary(consecutiveOne)))) * "0"
            return frontOne + str(numToBinary(consecutiveOne)) + compress_helperZero(S, 0)

    return compress_helperZero(S, 0)
        
def uncompress(C):
    '''"Inverts" or "undoes" the compressing in the compress function.'''
    def uncompress_helperZero(C, k):
        '''Outputs the uncompressed component for the 0.'''
        if C == "":
            return ""
        else:
            return "0" * binaryToNum(C[:k]) + uncompress_helperOne(C[k:],k)

    def uncompress_helperOne(C, k):
        '''Outputs the uncompressed component for the 1.'''
        if C == "":
            return ""
        else:
            return "1" * binaryToNum(C[:k]) + uncompress_helperZero(C[k:],k)

    return uncompress_helperZero(C, COMPRESSED_BLOCK_SIZE)

'''For the case where k = 5, 325 bits are the maximum number
of bits the compress algorithm would use. This is because if the sequence would start
with a 10 and repeat 32 times, each of the 64 bits would be displayed as 5 bits.
Therefore, 64 * 5 = 320, and when we start with 1, we add 5 more bits to
dsiplay the amount of 0 terms. Now, 320 + 5 = 325.'''

def compression(S):
    '''Returns the ratio of the compressed size to the original size for image S.'''
    return len(compress(S))/len(S)

'''I conducted tests with compressions of (64*'0'),(64*'1'),(32*'01'),(32*'10'),
(16*'1001'), and (16*'0110'). However, only (64*'0') and (64*'1') resulted in answers
less than 1. This shows that the compression of a string with a lot of the
same numbers in a row has the smallest ratio.'''

'''This algorithm can't exist since there will always be a case,
such as a string constantly interchanging 0's and 1's, where it would require more bits to
represent both the amount of bits and the change in bits than there initially were
in the given string.'''

        
