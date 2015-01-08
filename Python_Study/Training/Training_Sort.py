"""Training_sord"""
def num_sorr(num):
    """Return Sord number"""
    num_list = [input() for _ in xrange(num)]
    num_sord = quicksord(num_list)
    for number in num_sord:
        print number
def quicksord(lst):
    """return List already sord"""
    if not lst:
        return []
    return (quicksord([x for x in lst[1:] if x < lst[0]])
            + [lst[0]] +
            quicksord([x for x in lst[1:] if x >= lst[0]]))
num_sorr(int(raw_input()))
