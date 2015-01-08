'''Parallelism'''
#Comment

def slope():
    '''DocString'''
    do1 = input()
    ti1 = input()
    do2 = input()
    ti2 = input()
    do3 = input()
    ti3 = input()
    do4 = input()
    ti4 = input()
    sum1 = (do2 - do1)
    sum2 = (ti2 - ti1)
    sum3 = (do4 - do3)
    sum4 = (ti4 - ti3)
    if sum2 == 0 or sum4 == 0:
        if sum2 == sum4:
            print 'YES'
        else:
            print 'NO'
    elif sum1 / sum2 == sum3 / sum4:
        print 'YES'
    else:
        print 'NO'
slope()
