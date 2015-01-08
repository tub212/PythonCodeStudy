"""Lab_EuclideanDistance"""
def eucdis(point, num_ls=list()):
    """return dictance of point 1 to point input"""
    num = [raw_input() for _ in xrange(point)]
    for att in xrange(len(num) - 1):
        do1, do2 = map(int, num[att].split()), map(int, num[att+1].split())
        num_ls.append(((do1[0] - do2[0])**2 + (do1[1] - do2[1])**2)**0.5)
    return format(sum(num_ls), "0.2f")
print eucdis(input())
