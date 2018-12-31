'''Edward Yaroslavsky eyarosla 10/21/18
I pledge my honor that I have abided by the Stevens Honor System.'''

FullAdder = { ('0','0','0') : ('0','0'),('0','0','1') : ('1','0'),('0','1','0') : ('1','0'),('0','1','1') : ('0','1'),('1','0','0') : ('1','0'),('1','0','1') : ('0','1'),('1','1','0') : ('0','1'),('1','1','1') : ('1','1') }

def numToBaseB(N, B):
    '''Converts a number, N, to a base, B.'''
    if N == 0:
        return "0"

    def numToBaseBHelper(N, B):
        '''Converts a number, N, to a base, B.'''
        if N == 0:
            return ""
        else:
            return numToBaseBHelper(N//B,B) + str(N % B)

    return numToBaseBHelper(N, B)

def baseBToNum(S, B):
    '''Converts S from base B into base 10.'''
    if S == "":
        return 0
    elif S[0] == "0":
        return baseBToNum(S[1:], B)
    else:
        return int(S[0])*(B**(len(S)-1)) + baseBToNum(S[1:], B)

def baseToBase(B1,B2,SinB1):
    '''Converts SinB1 from base B1 into base B2.'''
    return numToBaseB(baseBToNum(SinB1,B1),B2)

def add(S,T):
    '''Adds the binary Strings S and T by converting into base 10 first and
    then re-converting into base 2.'''
    return numToBaseB(baseBToNum(S,2)+baseBToNum(T,2),2)

def addB(S,T):
    '''Adds the binary Strings S and T by using carry bits.'''
    def addBHelper(S,T,carryBit):
        '''Adds the binary Strings S and T by using carry bits.'''
        if S == "" and carryBit == "1" and T == "1":
            return '10'
        elif S == "" and carryBit == "1" and T == "0":
            return '1'
        if T == "" and carryBit == "1" and S == "1":
            return '10'
        elif T == "" and carryBit == "1" and S == "0":
            return '1'
        elif S == "":
            return T
        elif T == "":
            return S
        else:
            sumBit, carryBit = FullAdder[(S[-1],T[-1],carryBit)]
            return addBHelper(S[:-1],T[:-1],carryBit) + sumBit

    def removeLeadingZero(S):
        '''Removes the leading '0' values from String S.'''
        if S[0] == "1":
            return S
        return removeLeadingZero(S[1:])

    return removeLeadingZero(addBHelper(S,T,'0'))
