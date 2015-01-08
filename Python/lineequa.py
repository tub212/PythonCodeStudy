"""LinearEquation"""
###Comment
def lineequa(number):
    """Find Max min and avg"""
    num = number.split()
    num = [float(i) for i in num]
    num[2] = 0 - num[2]
    num[5] = 0 - num[5]
    y_sum = (num[5]*num[0]-num[3]*num[2])/(num[0]*num[4]-num[3]*num[1])
    if num[0] != 0:
        x_sum = (num[2]-num[1]*y_sum)/(num[0])
        print "x = "+str("%.3F" % (x_sum))
    else:
        x_sum = (num[5]-num[4]*y_sum)/(num[3])
        print "x = "+str("%.3F" % (x_sum))
    if y_sum == 0:
        y_sum = abs(y_sum)
        print "y = "+str("%.3F" % (y_sum))
    else:
        print "y = "+str("%.3F" % (y_sum))
lineequa(raw_input())
