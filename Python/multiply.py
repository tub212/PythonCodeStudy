"""Multiply|Recursion"""
#COMMENT
def multiply(number1, number2):
    """Multiply Number"""
    if number1 >= 0 and number2 >= 0: #+,+
        if number1 > 0:
            return multiply(number1-1, number2) + number2
    elif number1 < 0 and number2 > 0: #-,+
        if number1 < 0:
            return multiply(number1+1, number2) - number2
    elif number1 > 0 and number2 < 0: #+,-
        if number1 > 0:
            return multiply(number1-1, number2) + number2
    elif number1 < 0 and number2 < 0: #-,-
        number1, number2 = abs(number1), abs(number2)
        if number1 > 0:
            return multiply(number1-1, number2) + number2
    return 0
print multiply(input(), input())
