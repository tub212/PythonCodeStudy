'''Windmill'''
def windmill(row):
    '''Creat Willmill'''
    star = row
    space = row - 1
    for i in xrange(1, row+1):
        print '*'*i + ' '*space + '*'*star
        space -= 1
        star -= 1
    space = row-1
    star = row
    spacecenter = 0
    for j in xrange(1, row+1):
        print ' '*space + '*'*j + ' '*spacecenter + '*'*star
        space -= 1
        spacecenter += 1
        star -= 1
windmill(input())
