"""WTFFFFFFF"""
###comment
def jaa(mainsum, numbersum):
	"""Docsting"""
	print " _" * (mainsum)
    for i in xrange(mainsum):
        print "|" + "_|" * numbersum

def make(main, number):
    """DOcstirng2"""
    if main == number:
        jaa(main, number)
    elif main < number:
        main = main + (number - main)
        jaa(main, number)
    elif main > number:
        main = main  - (main - number)
        jaa(main, number)
make(input(), input())
