"""this program made X from star(*)"""
def printx():
    """input star length
    return a X with - betweent space
    """
    num = int(raw_input())-1
    for i in range(num) + range(num, -1, -1):
        if i == num:
            print "-"*num+"*"+"-"*num
        else:
            print "-"*i + "*" + "-"*((num-i)*2-1) + "*" + "-"*i
printx()
