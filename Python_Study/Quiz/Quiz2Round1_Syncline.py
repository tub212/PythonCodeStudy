"""Quiz2Round1_Syncline"""
def syncline(fst, scnd):
    """Return sum of char in st and nd"""
    if len(fst) > len(scnd):
        scnd = "0" * (len(fst) - len(scnd)) + scnd
        return sum([int(fst[i]) * int(scnd[i]) for i in xrange(len(fst))])
    elif len(fst) < len(scnd):
        fst = "0" * (len(scnd) - len(fst)) + fst
        return sum([int(fst[i]) * int(scnd[i]) for i in xrange(len(fst))])
    else:
        return sum([int(fst[i]) * int(scnd[i]) for i in xrange(len(fst))])
print syncline(raw_input(), raw_input())
