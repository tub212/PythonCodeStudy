'''pos_neg'''
#Comment

def pos_neg(number1, number2, boolean):
    '''3 lines = True or False'''
    if boolean == True:
        if number1 < 0 and number2 > 0:
            return "True"
        elif number1 > 0 and number2 < 0:
            return "True"
        else:
            return "False"
    if boolean == False:
        if number1 > 0 and number2 > 0:
            return "True"
        if number1 < 0 and number2 < 0:
            return "True"
        else:
            return "False"
print pos_neg(input(), input(), input())
