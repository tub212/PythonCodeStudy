'''Docstring'''
def pyramid(rows):
    for i in xrange(rows):
        print ' '*(rows-i-1) + 'A'*(2*i+1)
pyramid(input())        