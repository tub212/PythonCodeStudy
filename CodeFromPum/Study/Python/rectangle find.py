'''Rectangle'''
#Comment

def rectangle(longrec, wide):
    '''Find calculate rectangle size and length'''
    if longrec != wide:
        return str(longrec * wide) + "\n" + str((longrec * 2) + (wide * 2))
print rectangle(input(), input())
