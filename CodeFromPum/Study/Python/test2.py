startnumber=7
startnumber*=1.0
prime = True
for divisor in range(2,startnumber):
    if startnumber/divisor==int(startnumber/divisor):
        prime=False
if prime==False:
    print startnumber," is not prime"
else:
    print startnumber, "is prime"