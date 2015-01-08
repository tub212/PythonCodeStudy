"""Jellopyyyyy"""
def jelly(number):
    """JELLOPY"""
    numberls = map(int, number.split())
    numberls.sort()
    print numberls
    count = 0
    maxnum = numberls.pop(2)
    print maxnum
    while maxnum != 1:
        print maxnum
        if maxnum%2 == 0:
            maxnum = maxnum/2
            numberls.append(maxnum)
            count = count + 1
        else:
            maxnum -= 1
            maxnum = maxnum/2
            numberls.append(maxnum)
            count = count + 1
    print count
    print numberls
jelly(raw_input())
