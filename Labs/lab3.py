'''Edward Yaroslavsky eyarosla 9/20/18 
I pledge my honor that I have abided by the Stevens Honor System.'''

def change(amount, coins):
    '''Returns the minimum number of coins from the currency list, coins,
    it takes for the value, amount, to be made up.'''
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif amount < coins[-1]:
        return change(amount, coins[:-1])
    else:
        use = 1 + change(amount - coins[-1], coins)
        lose = change(amount, coins[:-1])
        return min(use, lose)
              
