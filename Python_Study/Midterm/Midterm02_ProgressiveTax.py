"""Midterm02_ProgressiveTax"""
def tax(money):
    """Return Pay tax money
    """
    if money <= 150000:
        print "0"
    elif money > 150000 and money <= 300000:
        print int((money - 150000) * (5.0 / 100))
    elif money > 300000 and money <= 500000:
        print int((money - 300000) * (10.0 / 100)) + 7500
    elif money > 500000 and money <= 750000:
        print int((money - 500000) * (15.0 / 100)) + 27500
    elif money > 750000 and money <= 1000000:
        print int((money - 750000) * (20.0 / 100)) + 65000
    elif money > 1000000 and money <= 2000000:
        print int((money - 1000000) * (25.0 / 100)) + 115000
    elif money > 2000000 and money <= 4000000:
        print int((money - 2000000) * (30.0 / 100)) + 365000
    elif money > 4000000:
        print int((money - 4000000) * (35.0 / 100)) + 965000
tax(input())
