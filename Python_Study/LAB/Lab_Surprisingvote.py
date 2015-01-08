"""This program check possibility of Surprise vote"""
def surprisingvote(score, high):
    """input Sum of all score and highest score
    return Surprising or not surprising
    """
    lowest = score - (high * 2)
    if lowest < 0:  
        lowest = 0
    if high - lowest > 2:
        print "surprising"
    else :
        print "not surprising"
surprisingvote(int(raw_input()), int(raw_input()))
