"""Show "almost" lowest number"""
def almstmin():
    """input how many number you want then input number"""
    round_ = input()
    if round_ > 1:
        lowest = 1000
        alms = 1000
    for new in range(round_):
        new = input()
        if new < lowest:
            alms = lowest
            lowest = new
        elif new == lowest:
            lowest = new
        elif new < alms:
            alms = new
            if lowest == alms:
                print "NONE"
            else:
                print alms
        else:
            print "NONE"
almstmin()
