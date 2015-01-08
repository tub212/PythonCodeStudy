"""Lab_AllSameDigit"""
def same(numstring, numcheck):
    """return yes or no if number check all same in
    in numstring"""
    listnum = map(int, numstring)
    return "yes" if listnum.count(numcheck) == len(numstring) else "no"
print same(raw_input(), input())
