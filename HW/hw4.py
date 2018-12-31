'''Edward Yaroslavsky eyarosla 10/1/18
I pledge my honor that I have abided by the Stevens Honor System.'''

def combine(L):
    '''Returns a list of the sums of all the two adjacent elements in the list, L.'''
    if L == [] or L == [1]:
        return []
    return [L[0]+L[1]] + combine(L[1:])

def pascal_row(n):
    '''Outputs a list of elements found in a certain row of Pascal’s Triangle.'''
    if n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    else:
        return [1] + combine(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    '''Takes as input a single integer n and returns a list of all the pascal_rows
    up to and including row n.'''
    if n == 0:
        return [pascal_row(0)]
    return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    '''Tests that pascal_row works as it should.'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(2) == [1,2,1]
    assert pascal_row(5) == [1,5,10,10,5,1]

def test_pascal_triangle():
    '''Tests that pascal_triangle works as it should.'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1],[1,1]]
    assert pascal_triangle(2) == [[1],[1,1],[1,2,1]]
    assert pascal_triangle(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]
