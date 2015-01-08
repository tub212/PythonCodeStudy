'''compare betweem binary number'''
#comment
def compare_binary(value1, value2):
    '''Check Binary'''
    if value1 > value2:
        return "1 0"
    elif value1 < value2:
        return "0 1"
    elif value1 == value2:
        return "1 1"

print compare_binary(input(), input())                