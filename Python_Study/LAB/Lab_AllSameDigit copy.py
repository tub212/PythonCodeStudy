'''Lab_AllSameDigit'''
def same(num, number):
    '''
input => number
output = > number'''
    for i in xrange(len(num)):
        if int(num[i]) != number:
            return 'no'
    return 'yes'
print same(raw_input(), input())
