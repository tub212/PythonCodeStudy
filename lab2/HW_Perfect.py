"""HW_Perfect"""
def is_prime(number):
    """Returns True if the number is prime
    else False."""
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True

def perfectnum(number):
    """return sum of perfect number from 1 to $number"""
    for i in xrange(2, number+1):
        if (2**(i-1))*(2**(i)-1) > number:
            prime_want = i
            break
    prime = filter(is_prime, range(1, prime_want))
    return sum(map(lambda i: (2**(i-1))*(2**(i)-1), prime))
print perfectnum(int(raw_input()))
