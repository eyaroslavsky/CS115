def mySum(L):
    '''sum(L), assuming L is a list of numbers'''
    if L == []:
        return 0
    else:
        return L[0] + mySum(L[1:])
