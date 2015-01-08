"""Total Circular Prime"""
def cirprime(number):
    """Check is it Circular Prime"""
    numchecker = str(number)
    for _ in xrange(len(numchecker)):
        if not isprime(int(numchecker)):
            return 0
        numchecker = numchecker[1:] + numchecker[0]
    return number

def isprime(numcheck):
    """Check if number is Prime"""
    for i in xrange(2, int(numcheck ** 0.5) + 1):
        if numcheck % i == 0:
            return False
    return True

def loop(num):
    """Return Sum of Circular Prime"""
    total = 0
    for i in xrange(2, num + 1):
        total += cirprime(i)
    return total

print loop(input())
