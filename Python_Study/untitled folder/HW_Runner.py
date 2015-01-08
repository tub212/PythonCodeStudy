"""HW_Runner"""
def winnerplayer(distance, player):
    """Find the winner of this competition"""
    speed, start = map(list, zip(*[map(int, raw_input().split())\
                                   for _ in xrange(player)]))
    while max(start) < distance:
        for i in xrange(player):
            start[i] += speed[i]
            speed[i] *= 2
    if start.count(max(start)) > 1:
        return speed.index(max([speed[j] for j in start if j == max(start)]))
    return start.index(max(start)) + 1
print winnerplayer(input(), input())
