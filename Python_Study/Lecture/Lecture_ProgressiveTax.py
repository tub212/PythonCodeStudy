"""Lecture_ProgressiveTax"""
def taxpay(tax):
    """Return tax to pay to Gov"""
    tax5 = 150000*(0.05)
    tax10 = 200000*(0.1)
    tax15 = 250000*(0.15)
    tax20 = 250000*(0.2)
    tax25 = 1000000*(0.25)
    tax30 = 2000000*(0.3)
    if tax <= 150000:
        print "0"
    elif tax > 150000 and tax <= 300000:
        print int((tax - 150000)*(0.05))
    elif tax > 300000 and tax <= 500000:
        print int((tax - 300000)*(0.1) + tax5)
    elif tax > 500000 and tax <= 750000:
        print int((tax - 500000)*(0.15) + (tax5 + tax10))
    elif tax > 750000 and tax <= 1000000:
        print int((tax - 750000)*(0.20) + (tax5 + tax10 + tax15))
    elif tax > 1000000 and tax <= 2000000:
        print int((tax - 1000000)*(0.25) + (tax5 + tax10 + tax15 + tax20))
    elif tax > 2000000 and tax <= 4000000:
        print int((tax - 2000000)*(0.30) + (tax5 + tax10 + tax15 + tax20 + \
                                        tax25))
    elif tax > 4000000:
        print int((tax - 4000000)*(0.35) + (tax5 + tax10 + tax15 + tax20 + \
                                        tax25 + tax30))
taxpay(input())
