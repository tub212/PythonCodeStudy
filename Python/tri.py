'''Make Triangle By Python'''
#COmment
def make_triangle(long1, long2, long3):
    '''Function Make Tirangle'''
    if long1 + long2 < long3:
        return "NO"
    elif long1 + long3 < long2:
        return "NO"
    elif long2 + long3 < long1:
        return "NO"
    else:
        return "YES"
print make_triangle(input(), input(), input())
