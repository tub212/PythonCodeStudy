"""PAT CAT"""
####commnet
def patcat(number1, number2):
    """Print PATCAT"""
    print ":"
    print ":-"
    for i in xrange(number1, number2, 2):
        print ":-" + ")"*i
patcat(1, 64)
