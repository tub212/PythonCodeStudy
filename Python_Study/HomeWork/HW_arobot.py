"""AROBOT"""
def chargebatt():
    """int -> int
        this programme is find a battery to change"""
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
    print count
def loopchrage(robot):
    """Loop Charge make to Debug the chargebatt"""
    count = robot
    while count > 0:
        chargebatt()
        count -= 1
loopchrage(int(raw_input()))
