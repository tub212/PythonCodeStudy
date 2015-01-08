"""Check 90 Triangle"""
def triangle(side1, side2, side3):
    """This Programme Check A Triangle is a 90 triangle"""
    if (side1)**2 + (side2)**2 == (side3)**2:
        print "Yes."
    elif (side1)**2 + (side3)**2 == (side2)**2:
        print "Yes."
    elif (side2)**2 + (side3)**2 == (side1)**2:
        print "Yes."
    else:
        print "No."    
triangle(int(raw_input()), int(raw_input()), int(raw_input()))
