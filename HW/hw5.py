'''
Created on 10/9/18
@author: Edward Yaroslavsky eyarosla
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

width = 16
turtle.left(90)
turtle.pencolor("brown")
turtle.width(width)
def sv_tree(trunk_length, levels):
    '''Draws a tree of levels amount of recursive branches with decreasing
    trunk_length size after every level.'''
    if levels > 0:
        if levels == 1:
            turtle.pencolor("green")
        else:
            turtle.pencolor("brown")
        turtle.forward(trunk_length)
        turtle.width(width // 2)
        turtle.right(30)
        sv_tree(trunk_length // 2, levels - 1)
        turtle.left(60)
        sv_tree(trunk_length // 2, levels - 1)
        turtle.right(30)
        turtle.penup()
        turtle.forward(-1 * trunk_length)
        turtle.pendown()

memoList = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in memoList:
        return memoList[n]
    elif n == 0:
        memoList[n] = 2
        return 2
    elif n == 1:
        memoList[n] = 1
        return 1
    else:
        memoList[n] = fast_lucas(n-1) + fast_lucas(n-2)
        return fast_lucas(n-1) + fast_lucas(n-2)

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount,coins) in memo:
            return memo[(amount,coins)]
        elif amount == 0:
            memo[(amount,coins)] = 0
            return 0
        elif coins == ():
            memo[(amount,coins)] = float("inf")
            return float("inf")
        elif amount < 0:
            memo[(amount,coins)] = float("inf")
            return float("inf")
        else:
            use = 1 + fast_change_helper(amount - coins[0], coins, memo)
            lose = fast_change_helper(amount, coins[1:], memo)
            memo[(amount,coins)] = min(use, lose)
            return min(use, lose)
    return fast_change_helper(amount, tuple(coins), {})


# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


# Should take a few seconds to draw a tree.
sv_tree(128, 4)
turtle.bye()
