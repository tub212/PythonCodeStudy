"""HW_HaPaSi"""
def hapasi():
    """Find the winner of HaPaSi"""
    condition_type = [["H - H", "P - P", "S - S"], ["H - S", "P - H", "S - P"]]
    a_score, b_score, draw_score = 0, 0, 0
    round_play = 1
    while True:
        play_type = raw_input()
        if play_type in condition_type[0]:
            draw_score += 1
            if draw_score == 5:
                return "NONE\n"+str(round_play)
        elif play_type in condition_type[1]:
            draw_score = 0
            a_score += 1
            if a_score == 5:
                return "A\n"+str(round_play)
        else:
            draw_score = 0
            b_score += 1
            if b_score == 5:
                return "B\n"+str(round_play)
        round_play += 1

print hapasi()
