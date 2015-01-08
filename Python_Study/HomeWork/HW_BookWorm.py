"""HW_BookWorm"""
def bookworm(people):
    """Return Number of book of people can read"""
    for _ in xrange(people):
        tme, bok, r_t, r_b = input(), [input() for _ in xrange(input())], 0, 0
        bok.sort()
        for i in xrange(len(bok)):
            if (r_t + bok[i]) <= tme:
                r_t, r_b = r_t + bok[i], r_b + 1
        print r_b           
bookworm(input())
