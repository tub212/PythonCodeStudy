'''Factorial-ial-ial'''
###commnet
def fac(num, fact):
    '''find_value_factorial'''
    fact = len(fact)
    value = 1
    if num == 0:
        print 1
    elif num == 1:
        print 1
    elif num % fact == 0:
        while num != fact:
            value = value*num
            num -= fact
            if num == fact:
                value = value*num
                print value
                break
    else:
        while num != num%fact:
            value = value*num
            num -= fact
            if num == num%fact:
                value = value*num
                print value
                break
fac(input(), raw_input())
