'''Fibonacci'''
def fibo(number):
    '''
    return fibonucci of input
    '''
    if number == 1 or number == 0:
        return number
    return fibo(number-1) + fibo(number-2)
print fibo(input())
