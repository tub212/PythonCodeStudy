'''This programme will find a collatz calculation'''
number = input()
print number
while number != 1:
    if number % 2 != 0:
        number = 3*(number)+1
        print number
    else:
        number = number/2
        print number    