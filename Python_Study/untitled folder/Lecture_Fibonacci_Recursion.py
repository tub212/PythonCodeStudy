"""Lecture_Fibonacci_Recursion"""
def fibo(pos):
    """Return Fibonacci NUmber"""
    if pos < 2:
        return pos
    return fibo(pos-1) + fibo(pos-2)
print fibo(input())
