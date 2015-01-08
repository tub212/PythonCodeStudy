"""Divide3or5"""
def divide(num):
    """return Sum of number divi by 3 or 5"""
    return sum(filter(lambda x: x%3 == 0 or x%5 == 0, xrange(1, num+1)))
print divide(input())
