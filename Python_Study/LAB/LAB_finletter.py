"""LAb_Findletter"""
def findletter(word, string):
    """
    STR -> int
    This programme count string in the word
    """
    word = word.lower()
    string = string.lower()
    count = 0
    for i in word:
        if i == string:
            count += 1
    print count
findletter(raw_input(), raw_input())
