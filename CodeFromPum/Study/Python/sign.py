"""Sign"""
##comment
def sign(line1, line2, line3):
    """Print String Inverse"""
    lineprint = max(len(line1), len(line2), len(line3))
    if len(line1) != lineprint:
        addstr = lineprint - len(line1)
        line1 = line1 + " "*addstr
    if len(line2) != lineprint:
        addstr = lineprint - len(line2)
        line2 = line2 + " "*addstr
    if len(line3) != lineprint:
        addstr = lineprint - len(line3)
        line3 = line3 + " "*addstr
    for i in xrange(lineprint):
        print line1[i], line2[i], line3[i]
sign(raw_input(), raw_input(), raw_input())
