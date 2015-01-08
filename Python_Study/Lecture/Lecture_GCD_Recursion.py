"""Lecture_GCD_Recursion"""
def gcdrecursion(num1, num2):
    """Return GCD number between num1 & num2"""
    if num2 == 0:
        return num1
    return gcdrecursion(num2, num1%num2)
print gcdrecursion(input(), input())
