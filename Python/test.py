n = input()
for i in xrange(1, n):
    def isprime(n):
        '''check if integer n is a prime'''
        n = abs(int(n))
        if n < 2:
            return False
        
        if n == 2: 
            return "2 is a prime number."    
        
        if not n & 1: 
            return False
        
        for x in range(3, int(n**0.5)+1, 2):
            if n % x != 0:
                return False
        return str(n)+" is a prime number."
    print isprime(i)    