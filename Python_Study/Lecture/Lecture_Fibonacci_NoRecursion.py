"""Lecture_Fibonacci_NoRecursion"""
def fibo(pos):
    """return Fibonacci number"""
    if pos in [0, 1]:
        return pos
    num1, num2 = 0, 1
    for _ in xrange(2, pos+1):
        num1, num2 = num2, num1+num2
    return num2
print fibo(input())
