"""Lab_Missing"""
def missing(number):
    """
    return missing number between 1 to number
    """
    numls = range(number+1)
    numinp = -1
    while numinp != 0:
        numinp = int(raw_input())
        numls.remove(numinp)
    for i in numls:
        print i
missing(int(raw_input()))
