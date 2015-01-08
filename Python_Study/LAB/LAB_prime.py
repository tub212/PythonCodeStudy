"""prime number"""
def is_prime(number):
    """
    int -> int
    This programme is check prime number in range your input
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if not number & 1:
        return False
    for i in xrange(3, int(number**0.5)+1, 2):
        if number % i == 0:
            return False
    return True
def countprime(checknumber):
    """
    int -> int
    This programme is check prime number in range your input
    """
    count = 0
    for i in xrange(1, checknumber+1):
        answer = is_prime(i)
        if answer == True:
            count += 1
    print count
countprime(int(raw_input()))
