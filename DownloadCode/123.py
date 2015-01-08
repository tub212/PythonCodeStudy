"""AROBOT"""
def chargebatt(robot):
    """int -> int
        this programme is find a battery to change"""
    while robot > 0:
        vbatt = 0
        count = 0
        for j in xrange(int(raw_input())+1):
            if j == 0:
                vbatt = int(raw_input())
            else:
                batt = int(raw_input())
                if batt < vbatt:
                    count += 1
                else:
                    pass
        robot -= 1
        print count
chargebatt(int(raw_input()))
