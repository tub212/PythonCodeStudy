"""This programme find Overlaping between 2 Circle"""
def overlap():
    """ input == int
        output == overlaping or no overlapping
        This programme find Overlaping between 2 Circle"""
    cir1x = float(raw_input())
    cir1y = float(raw_input())
    rad1 = float(raw_input())
    cir2x = float(raw_input())
    cir2y = float(raw_input())
    rad2 = float(raw_input())
    radius = rad1 + rad2
    compare = ((cir2y - cir1y)**2 + (cir2x - cir1x)**2)**0.5
    if compare > radius:
        print "no overlapping"
    else:
        print "overlapping"
overlap()
