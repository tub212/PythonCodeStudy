"""HW_GCD_N"""
def gcd(num1, num2):
    """Find GCD between 2 number"""
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
def gcdn(numin):
    """Find gcd Number more than 2 number"""
    if numin == 1:
        print input()
    else:
        numls = [input() for _ in xrange(numin)]
        ans = gcd(numls[0], numls[1])
        for i in numls[2:]:
            ans = gcd(ans, i)
        print ans
gcdn(input())
