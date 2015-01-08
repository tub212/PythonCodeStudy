"""Lecture_GCD_Large"""
def gcdlarge(num1, num2):
    """Return GCD number"""
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    print num1
gcdlarge(input(), input())
