'''RightJustify'''
#Comment

def rightjustify(word, display):
    '''Docstring'''
    space = " " * (display - len(str(word)))
    return space + word
print rightjustify(raw_input(), input())
