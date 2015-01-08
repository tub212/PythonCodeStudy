"""Training_EuclideanDistance"""
def distance(time, num_ans=list(), num=list()):
    """Return Distance 1 to N"""
    for _ in xrange(time):
        numapp = raw_input()
        num.append(numapp)
    for att in xrange(len(num) - 1):
        do1, do2 = map(int, num(att).split()), map(int, num(att+1).split())
        num_ans.append(((do1(0) - do2(0))**2 + (do1(1) - do2(1))**2)**0.5)
    return format(sum(num_ans), "0.2f")
print distance(input())
