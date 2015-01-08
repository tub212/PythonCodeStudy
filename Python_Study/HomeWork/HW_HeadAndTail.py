"""HW_HeadAndTail"""
def headandtail(zigma, numls):
    """Return Sum of number in numls"""
    numls.sort()
    nummin, nummax = 0, 0
    for i in xrange(1, zigma+1):
        nummin += numls[i-1]
        nummax += numls[-i]
    print nummin + nummax
headandtail(input(), input())
