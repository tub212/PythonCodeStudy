"""TEST WRITer"""
def writer(sen):
    """Return Money to get back in thai bath"""
    lensen = len(sen)
    if lensen <= 10:
        print "Pr!ze:=> 0 bAtH"
    elif lensen >= 11 and lensen <= 30:
        print "Pr!ze:=> " + str(lensen*1.23) + " bAtH"
    elif lensen >= 31 and lensen <= 50:
        print "Pr!ze:=> " + str(lensen*4.56) + " bAtH"
    elif lensen >= 51:
        print "Pr!ze:=> " + str(lensen*9.99) + " bAtH"
writer(raw_input())
