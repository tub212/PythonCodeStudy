"""Lab_CoPrimeV1"""
def coprime(num1, num2):
    """
    return Yes or No and return GCD between 2 number
    """
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    if num1 == 1:
        print "YES" "\n" + str(num1)
    else:
        print "NO" "\n" + str(num1)
coprime(input(), input())
