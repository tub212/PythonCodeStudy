"""HW_Diff"""
def diff(num1, num2):
    """Return Diff of Sum"""
    sum1 = [i for i in xrange(num1, num2+1, 2)]
    sum2 = [j for j in xrange(num1+1, num2+1, 2)]
    print abs(sum(sum1) - sum(sum2))
diff(input(), input())
