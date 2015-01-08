"""HW_Sigmastep"""
def sigmastep(input1, input2, input3):
    '''input (start, stop, step -> sum of all number)'''
    if (input2-input1)*input3 >= 0 and input3!=0:
        num = range(input1, input2+input3/abs(input3), input3)
    count = 0
    for i in num:
        count += i
    return count
    return "error"
print sigmastep(input(), input(), input())
