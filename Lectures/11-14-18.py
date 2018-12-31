def ncommon(L,M):
    '''assume L,M are sorted and have no duplicates.
    Return len(intersect(L,M))'''
    #return len(filter(lambda x: x in M, L))
    count = 0
    i = 0
    j = 0
    while i < len(L) and j < len(M):
        if L[i] == M[j]:
            count += 1
            i += 1
            j += 1
        elif L[i] < M[j]:
            i += 1
        else:
            j += 1
    return count
