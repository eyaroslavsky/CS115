from cs115 import *

def ED(first, second):
    '''Returns the edit distance between the strings first and second.'''
    print("ED(" + first + "," + second + ")")
    if first == "":
        return len(second)
    elif second == "":
        return len(first)
    elif first[0] == second[0]:
        return ED(first[1:], second[1:])
    else:
        substitution = 1 + ED(first[1:], second[1:])
        deletion = 1 + ED(first[1:], second)
        insertion = 1 + ED(first, second[1:])
        return min(substitution, deletion, insertion)

def makeAt(strs):
    return map(lambda x: '@' + x[1:], filter(lambda x: x[0] == 'a' or x[0] == 'A', strs))
    
