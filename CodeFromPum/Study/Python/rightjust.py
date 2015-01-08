'''RightJustify'''
#Comment

def answer(display, text):
    '''Calculation space size.'''
    space = " " * ((display - len(text))/2)
    return space + text + space
print answer(input(), raw_input())
