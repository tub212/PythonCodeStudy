"""HorizontalHistogram"""
def islower(char):
    """return Lowwer Case of char"""
    char = ord(char)
    if char >= 97 and char <= 122:
        return True
    return False

def isupper(char):
    """return Upper Case of char"""
    char = ord(char)
    if char >= 65 and char <= 90:
        return True
    return False

def histrogram(string):
    """return Histogram of input string"""
    his = {}
    for i in string:
        his[i] = his.get(i, 0) + 1
    for i in sorted(his.keys()):
        out = ''
        if islower(i):
            his[i] -= 1
            out += '-----|'*(his[i]/5) + '-'*(his[i]%5) + '-'
            print i, ':', out
    for i in sorted(his.keys()):
        out = ''
        if isupper(i):
            his[i] -= 1
            out += '-----|'*(his[i]/5) + '-'*(his[i]%5) + '-'
            print i, ':', out
histrogram(raw_input())
