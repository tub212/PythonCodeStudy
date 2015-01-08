"""Lecture Fibonacci Recursion Memo"""
def fibo(num, fibo_dict):
    """Return Fibonacci number"""
    if num in fibo_dict:
        return fibo_dict[num]
    else:
        fibo_dict[num] = fibo(num-2, fibo_dict) + fibo(num-1, fibo_dict)
        return fibo_dict[num]
print fibo(input(), {0: 0, 1: 1})
