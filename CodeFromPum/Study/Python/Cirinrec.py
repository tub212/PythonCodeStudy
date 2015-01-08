'''Cirinrec'''
#Comment
def circle(rectangle1, rectangle2, circle1, circle2, radius):
    '''Docstring'''
    if rectangle1 - radius < circle1 or rectangle2 - radius < circle2:
        print "No"
    else:
        print "Yes"
circle(input(), input(), input(), input(), input())
