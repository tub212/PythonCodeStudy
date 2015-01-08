"""HW_PedPonFire"""
def ped(num):
    """return number of pair"""
    pedd, constant = [input() for _ in xrange(num)], input()
    pedd, ped2 = [x for x in pedd if x <= constant], dict()
    for i in pedd:
        if i in ped2:
            ped2[i] += 1
        else:
            ped2[i] = 1
    cnt1, pass_lst = 0, list()
    for i in ped2:
        if constant - i in pass_lst:
            pass
        elif constant - i == i:
            pass_lst.append(i)
            cnt1 += ped2[i] * (ped2[i] - 1)
        elif constant - i in ped2:
            pass_lst.append(i)
            cnt1 += ped2[i] * ped2[constant - i]
    return cnt1
print ped(input())