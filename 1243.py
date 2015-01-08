"""HW_Almstmin"""
def almstmin(line):
    """"""
    lsnum = []
    for i in xrange(line):
        number = int(raw_input())
        lsnum.append(number)
    lsnum.sort()
    check = min(lsnum)
    for l in lsnum:
        if l != check:
            print l
            break
        
almstmin(int(raw_input()))
