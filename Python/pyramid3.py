'''Docstring'''
def pyramid(rows):
    '''Docstring'''
    for i in reversed(xrange(rows)):
        print ' '*(rows-i-1) + '*'*(2*i+1)
pyramid(input())        