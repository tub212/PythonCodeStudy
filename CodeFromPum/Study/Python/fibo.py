"""Docstring"""
def fibonacci(number):
    """Find FIBO"""
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
print fibonacci(input())
