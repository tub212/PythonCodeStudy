'''jaaaaAAAzzzzzZZ'''
###comment

def grid(row, column):
    '''Making grid in N rows and M columns'''
    if row >= 1 and column >= 1:
        print " _" * column
        loop = row
        while loop != 0:
            print ("|_" * column) + "|"
            loop -= 1
grid(input(), input())
