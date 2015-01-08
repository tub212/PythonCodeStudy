def isprime(n):
	for x in range(1, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
print isprime(input())