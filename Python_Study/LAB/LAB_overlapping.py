"""This programme find Overlaping between 2 Circle"""
def overlap(cir1x, cir1y, rad1, cir2x, cir2y, rad2):
    """ input == int
        output == overlaping or no overlapping
        This programme find Overlaping between 2 Circle"""
    radius = rad1 + rad2
    compare = ((cir2y - cir1y)**2 + (cir2x - cir1x)**2)**0.5
    if compare > radius:
        print "no overlapping"
    else:
        print "overlapping"
overlap(float(raw_input()), float(raw_input()), float(raw_input()), \
        float(raw_input()), float(raw_input()), float(raw_input()))
