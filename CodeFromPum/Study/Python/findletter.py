"""Find Letter"""
###cOMMNet
def findlett(string, letter):
    """Find Letter in string input() and counting of letter"""
    string = string.upper()
    letter = letter.upper()
    count = 0
    for i in string:
        if i == letter:
            count += 1
    print count
findlett(raw_input(), raw_input())
