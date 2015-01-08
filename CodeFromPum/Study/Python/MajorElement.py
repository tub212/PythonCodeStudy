"""MajorElement"""
def checkmajor(number):
    """Check"""
    temp = number
    numberdict = {}
    number = number.split(",")
    for i in number:
        if i not in numberdict:
            numberdict[i] = 1
        else:
            numberdict[i] += 1
    highnumber = max(numberdict.values())
    if highnumber*1.0 > len(temp.split(","))/2.0:
        for j in numberdict:
            if numberdict[j] == highnumber:
                print j
                break
    else:
        print None
checkmajor(raw_input())
