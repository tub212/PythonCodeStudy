"""Chatacter"""
##comment
def char(string):
    """Find Upper And Lower letter in string and print number of character
        and print Upper and Lower case of string"""
    countup = 0
    countdown = 0
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90:
            countup += 1
        elif ord(i) >= 97 and ord(i) <= 122:
            countdown += 1
    print countdown, "\n", countup, "\n", string.lower(), "\n", string.upper()
char(raw_input())
