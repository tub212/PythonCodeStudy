"""Lab_OnetoTwo"""
def onetwo(num):
    """Return 21221 with number long"""
    if num == 1:
        return "1"
    elif num == 2:
        return "2"
    else:
        return onetwo(num-1) + onetwo(num-2)
print onetwo(input())
