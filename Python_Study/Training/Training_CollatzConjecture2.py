"""Training_CollatzConjecture"""
def conjec(num):
    """magic"""
    if num < 2:
        return num
    maxi = 0
    seq = dict()
    for j in xrange(3, num+1):
        cnt = 0
        while j != 1:
            if j in seq:
                cnt += seq[j]
                break
            if j % 2 == 0:
                j = j/2
            else:
                j = 3*j+1
            cnt += 1
        seq[j] = cnt
        if cnt + 1 > maxi:
            maxi = cnt + 1
    return maxi
print conjec(input())
