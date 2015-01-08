'''X2'''
number = input()
for i in xrange(-number+1, number):
    i_abs = abs(i)
    if i == 0:
        print ' '*(number-1-i_abs) + '*'
    else:
        print ' '*(number-1-i_abs) + '*' + ' '*(i_abs*2-1) + '*'    