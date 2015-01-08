"""Pre02_Maxnum"""
def maxnum(lis):
    """Return Max Number in list"""
    ans = []
    for i in lis:
        if isinstance(i, list):
            ans = ans + maxnum(i)
        else:
            ans.append(i)
    return ans
print max(maxnum(input()))
