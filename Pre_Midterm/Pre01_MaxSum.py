"""Pre01_MaxSum"""
def maxsum(num):
    """Return maxsum number as posible"""
    numlist = [abs(input()) for _ in xrange(num)]
    return sum(numlist)
print maxsum(input())
