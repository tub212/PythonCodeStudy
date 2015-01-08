"""HW_Than2"""
def than2(number):
    """
    return than2 number
    """
    if number > 1:
        return str(than2(number/2)) + str(number % 2)
    else:
        return str(number % 2)
print than2(input())
