"""Lab_Ball"""
def ball(position):
    """Return Position of Ball"""
    poss = [1, 0, 0]
    for i in position:
        if i == "A":
            poss[0], poss[1] = poss[1], poss[0]
        elif i == "B":
            poss[1], poss[2] = poss[2], poss[1]
        elif i == "C":
            poss[2], poss[0] = poss[0], poss[2]
    print poss.index(1) + 1
ball(raw_input())
