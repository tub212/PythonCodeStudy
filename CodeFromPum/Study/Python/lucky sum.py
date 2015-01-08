'''Luck_sum '''
#Comment

def lucky_sum(number1, number2, number3):
    '''Sum Lucky Number Not 13'''
    if number1 == 13:
        return "0"
    else:
        if number2 == 13:
            return number1
        else:
            if number3 == 13:
                return number1 + number2
            else:
                return number1 + number2 + number3
print lucky_sum(input(), input(), input())
