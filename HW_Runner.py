"""HW_Runner"""
def find_winnerofrunner(g_dis, a_p):
    """find the winner of running competition

    each player need to specific the speed and starting point
    example: 3 players
    6 2
    5 9
    1 4
    """
    p_spd, p_dis = map(list, zip(*[map(int, raw_input().split())\
                                   for _ in xrange(a_p)]))
    print p_spd
    print p_dis
    print a_p
    
    while max(p_dis) < g_dis:
        for i in xrange(a_p):
            p_dis[i] += p_spd[i]
            p_spd[i] *= 2
    if p_dis.count(max(p_dis)) > 1:
        return p_spd.index(max([p_spd[i] for i in p_dis if i == max(p_dis)]))
    return p_dis.index(max(p_dis))+1

print find_winnerofrunner(input(), input())
