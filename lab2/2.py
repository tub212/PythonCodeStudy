"""Lab_Factor"""


def factor(num):
    """print number that have maximum factor"""
    maxnum = 0
    max_lst = list()
    for _ in xrange(num):
        number = input()
        cnt = 0
        for i in xrange(1, number + 1):
            if number % i == 0:
                cnt += 1
        if cnt == maxnum:
            max_lst.append(number)
        elif cnt > maxnum:
            max_lst = [number]
            maxnum = cnt
    for i in max_lst:
        print i
factor(input())
