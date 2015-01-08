"""GCD"""
#Comment
def max_divi(number1, number2):
    """FIND GCD BETWEEN 2 NUMBER"""
    minnum = abs(min(number1, number2))
    maxnum = abs(max(number1, number2))
    if minnum == 0 and maxnum == 0:
        print "NONE"
    elif minnum == 0:
        print maxnum
    elif maxnum % minnum == 0:
        print minnum
    else:
        maxnum = maxnum % minnum
        max_divi(maxnum, minnum)
max_divi(input(), input())
