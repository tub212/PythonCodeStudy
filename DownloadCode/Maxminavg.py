"""Maxminavg"""
def maxminavg(number):
    """This functoin will mav min and average"""
    listnumber = map(int, number.split())
    print max(listnumber), "\n", min(listnumber)
    print sum(listnumber)/float(len(listnumber))
maxminavg(raw_input())
