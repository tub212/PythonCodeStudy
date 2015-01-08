"""Lecture_GCD_NoRecursion_Small"""
def gcd(num1, num2):
    """
    return GCD between 2 number
    """
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    print num1
gcd(input(), input())
