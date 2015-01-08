number = input()
def isprime(startnumber):
    startnumber *= 1.0
    for divisor in xrange(2,int(startnumber**0.5)+1):
        if startnumber/divisor == int(startnumber/divisor):
            return False
    return True
for i in range(2, number+1):
	if isprime(i):
		print str(i) +" is a prime number."  