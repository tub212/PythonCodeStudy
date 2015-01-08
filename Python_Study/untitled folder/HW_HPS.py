"""HW_HPS"""
def hps():
    """Return Winner of this games"""
    condition_type = [["H - H", "P - P", "S - S"], ["H - S", "P - H", "S - P"]]
    a_win, b_win, draw, round_att = 0, 0, 0, 1
    while True:
        atttempt = raw_input()
        if atttempt in condition_type[0]:
            draw += 1
            if draw == 5:
                return "NONE\n"+str(round_att)
        elif atttempt in condition_type[1]:
            draw = 0
            a_win += 1
            if a_win == 5:
                return "A\n"+str(round_att)
        else:
            draw = 0
            b_win += 1
            if b_win == 5:
                return "B\n"+str(round_att)
        round_att += 1
print hps()
