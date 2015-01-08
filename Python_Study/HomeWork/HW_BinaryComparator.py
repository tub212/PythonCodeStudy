"""HW_BinaryComparator"""
def binarycompare(num1, num2):
    """Return 1 0 if num1 > num2
        return 01 if num2 > num1
        return 1 1 if num1 == num2"""
    if num1 > num2:
        print "1 0"
    elif num2 > num1:
        print "0 1"
    elif num1 == num2:
        print "1 1"
binarycompare(input(), input())
