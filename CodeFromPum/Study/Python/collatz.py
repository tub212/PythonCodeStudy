'''Collatz'''
###comment
num1 = input()
print num1
while num1 != 1:
    if num1 % 2 != 0:
        num1 = 3*(num1)+1
        print num1
    else:
        num1 = num1/2
        print num1
    