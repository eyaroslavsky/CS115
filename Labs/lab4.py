'''Edward Yaroslavsky eyarosla 9/27/18 
I pledge my honor that I have abided by the Stevens Honor System.
Lab 4'''

def condense(L):
    '''Returns the sum of all the non-list elements in a list'''
    if L == []:
        return 0
    elif isinstance(L[0], list):
        return condense(L[1:])
    return L[0] + condense(L[1:])

def knapsack(capacity, itemList):
    '''Returns both the maximum value and the list of items that make up this value,
    without exceeding the capacity of the knapsack.'''
    if capacity == 0:
        return [0,[]]
    elif itemList == []:
        return [0,[]]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        use = condense([itemList[0][1],[]] + knapsack(capacity - itemList[0][0], itemList[1:]))
        lose = condense(knapsack(capacity, itemList[1:]))
        if use > lose:
            return [use, [itemList[0]] + knapsack(capacity - itemList[0][0], itemList[1:])[1]]
        else:
            return [lose, knapsack(capacity, itemList[1:])[1]] 

