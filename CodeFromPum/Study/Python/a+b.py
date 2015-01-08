"""A+BProblemPlus"""
###Comment
def aplusb(number):
    """Find sum of a and b"""
    for sumnum in xrange(number):
        sumnum = raw_input()
        sumnum = map(int, sumnum.split())
        print sum(sumnum)
aplusb(input())
