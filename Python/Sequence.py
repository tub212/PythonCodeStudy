"""SequencesDiff"""
###Comment
def sequence(number):
    """Sequence"""
    listnumber = number.split()
    listnumber = [int(i) for i in listnumber]
    step = listnumber[1] - listnumber[0]
    startcount = 2
    while startcount < len(listnumber):
        if listnumber[startcount] - step != listnumber[startcount-1]:
            print listnumber[startcount]
            break
        else:
            pass
        startcount += 1
sequence(raw_input())

