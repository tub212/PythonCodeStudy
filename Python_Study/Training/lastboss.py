"""LastBoss"""
def sum_all_number(num_ls):
    """return 1 digit of all sum number"""
    return sum(num_ls) if sum(num_ls) <= 9 else sum(map(int, str(sum(num_ls))))
def lastboss(point, summa, count=0):
    """Return Number of sum in range point"""
    for i in xrange(10**(point-1), 10**(point)):
        sum_ls = map(int, str(i))
        if sum_all_number(sum_ls) == summa:
            count += 1
    print count
lastboss(input(), input())
