"""Midterm01_Key"""
def key(num):
    """Return Key Of ID number"""
    numli = [int(i) for i in num]
    ansnum = sum(numli) + int(num[10:])*10
    if len(str(ansnum)) > 4:
        ans = str(ansnum)
        print ans[len(ans)-4:]
    elif len(str(ansnum)) < 4:
        print ansnum + 1000
    else:
        print ansnum
key(raw_input())
