"""PostQuiz1Round1dot2_IndicatorLeft"""
def indecator(length, tall):
    """Return Indecator left"""
    tall = tall/2
    for i in reversed(xrange(1, tall+1)):
        print " "*i + "*"*length
    for j in xrange(tall+1):
        print " "*j + "*"*length
indecator(input(), input())
 
