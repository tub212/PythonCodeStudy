"""HW_Perfect"""
def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
def perfect(num):
    """return sum of perfect number from 1 to $num"""
    for i in xrange(2, num+1):
        if (2**(i-1))*(2**(i)-1) > num:
            prime_want = i
            break
    prime = filter(is_prime, range(1, prime_want))
    return sum(map(lambda i: (2**(i-1))*(2**(i)-1), prime))

print perfect(input())
