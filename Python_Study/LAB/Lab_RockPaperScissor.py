"""Lab_RockPaperScissor"""
def rps(att, win_a=0, win_b=0):
    """Return Winner or Draw of this Game"""
    for i in xrange(0, len(att), 2):
        if att[i:i+2] == "RS" or att[i:i+2] == "PR" or att[i:i+2] == "SP":
            win_a += 1
        elif att[i:i+2] == "SR" or att[i:i+2] == "RP" or att[i:i+2] == "PS":
            win_b += 1
    return "A win " + str(win_a) + "-" + str(win_b) if win_a > win_b else \
           ("B win " + str(win_b) + "-" + str(win_a) if win_a < win_b else\
            "DRAW " + str((win_a + win_b) / 2))
print rps(raw_input())
