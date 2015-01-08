"""Diginity"""
def sumans(ans):
    """retrun Sum ans Number"""
    anscount = 0
    if len(ans) == 1:
        return ans
    else:
        for i in ans:
            anscount += int(i)
        return sumans(str(anscount))
def digit():
    """Return Code For one person"""
    ans = 1
    ansli = []
    while ans != 0:
        ans = input()
        if ans == 0:
            break
        else:
            answer = sumans(str(ans))
            ansli.append(answer)
    for j in ansli:
        print int(j)
digit()
