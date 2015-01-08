"""MAXMINAVG"""
###Comment
def maxminavg(number):
    """Find Max min and avg"""
    listnumber = number.split()
    listnumber = [int(i) for i in listnumber]
    print max(listnumber), "\n", min(listnumber)
    print sum(listnumber)/float(len(listnumber))
maxminavg(raw_input())
