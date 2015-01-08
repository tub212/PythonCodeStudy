"""Palindome"""
##Comment
def palin(number):
    """Palindome"""
    for string in xrange(number):
        string = raw_input()
        if string[::1] == string[::-1]:
            print string
palin(input())
