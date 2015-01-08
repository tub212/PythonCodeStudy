"""Lecture_Scout"""
def scout(data1, data2):
    """Return Value of EGG in a pot"""
    [t_egg, m_egg, m_weight] = data1
    data2.sort()
    t_weight = 0
    num_egg = 0
    while num_egg + 1 <= t_egg and num_egg + 1 <= m_egg and \
          t_weight + data2[num_egg] <= m_weight:
        t_weight = t_weight + data2[num_egg]
        num_egg = num_egg + 1
    return num_egg
def getans(case):
    """Return all case in def scout"""
    for _ in xrange(case):
        data1 = [int(j) for j in raw_input().split()]
        data2 = [int(k) for k in raw_input().split()]
        print scout(data1, data2)
getans(input())
