"""DeepLenV0"""
def deep(lis):
    """DeeplenV0"""
    count = 0
    for item in lis:
        if type(item) != list:
            count += 1
        else:
            count += deep(item)
    return count
print deep(input())
